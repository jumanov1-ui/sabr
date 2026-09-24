"""Higgsfield API example: generate a video with Seedance 2.5 (text-to-video).

Credentials are read at runtime from .env.local (HF_KEY="key-id:key-secret").
They are never printed or logged.
"""

import sys
from pathlib import Path

import httpx
from dotenv import load_dotenv

# Load credentials before importing the SDK usage below; override=False keeps
# any value already set in the real environment.
load_dotenv(Path(__file__).resolve().parent / '.env.local', override=False)

import higgsfield_client  # noqa: E402
from higgsfield_client import (  # noqa: E402
    NSFW,
    Cancelled,
    Completed,
    Failed,
    InProgress,
    Queued,
)
from higgsfield_client.exceptions import (  # noqa: E402
    CredentialsMissedError,
    HiggsfieldClientError,
)

MODEL = 'bytedance/seedance-2.5/text-to-video'
ARGUMENTS = {
    'prompt': 'A cinematic scene at sunset',
    'duration': 5,
    'resolution': '720p',
    'aspect_ratio': '16:9',
}

FAILURE_MESSAGES = {
    Failed: 'Generation failed.',
    Cancelled: 'Generation was canceled.',
    NSFW: 'Generation was blocked by content moderation.',
}


def find_video_url(result):
    """Return the video URL from a completed result, or None if absent."""
    if not isinstance(result, dict):
        return None
    video = result.get('video')
    if isinstance(video, dict) and video.get('url'):
        return video['url']
    videos = result.get('videos')
    if isinstance(videos, list) and videos and isinstance(videos[0], dict):
        return videos[0].get('url')
    return None


def main():
    final_status = {'value': None}

    def on_enqueue(request_id):
        print(f'Request enqueued: {request_id}')

    def on_queue_update(status):
        final_status['value'] = status
        if isinstance(status, Queued):
            print('Status: queued')
        elif isinstance(status, InProgress):
            print('Status: in progress')

    try:
        result = higgsfield_client.subscribe(
            MODEL,
            arguments=ARGUMENTS,
            on_enqueue=on_enqueue,
            on_queue_update=on_queue_update,
        )
    except CredentialsMissedError:
        print('Error: HF_KEY is not set. Add it to .env.local as key-id:key-secret.', file=sys.stderr)
        return 1
    except HiggsfieldClientError as error:
        print(f'Error: Higgsfield API request failed: {error}', file=sys.stderr)
        return 1
    except httpx.HTTPError as error:
        print(f'Error: could not reach the Higgsfield API: {error}', file=sys.stderr)
        return 1

    status = final_status['value']
    for status_type, message in FAILURE_MESSAGES.items():
        if isinstance(status, status_type):
            print(f'Error: {message}', file=sys.stderr)
            return 1

    if not isinstance(status, Completed):
        print(f'Error: request ended without completing (last status: {status}).', file=sys.stderr)
        return 1

    video_url = find_video_url(result)
    if not video_url:
        print('Error: request completed but no video URL was found in the response.', file=sys.stderr)
        return 1

    print(f'Video URL: {video_url}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
