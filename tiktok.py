from helpers import process_results
import sys
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(script_dir, 'tiktokanalytics', 'Lib', 'site-packages')

# Add the module directory to the Python path
sys.path.append(module_path)

from TikTokApi import TikTokApi
import asyncio
import pandas as pd

def get_data(hashtag):
    ms_token = os.environ.get("YOUR_MS_TOKEN_HERE", None) # get your own ms_token from your cookies on tiktok.com

    async def get_hashtag_videos(hashtag):
        async with TikTokApi() as api:
            await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
            # Get data by hashtag
            tag = api.hashtag(name=hashtag)
            videos_data = []  # List to store video data as dictionaries
            async for video in tag.videos(count=30):
                videos_data.append(video.as_dict)

            # Process data
            flattened_data = process_results(videos_data)

            # Convert preprocessed data to dataframe
            df = pd.DataFrame.from_dict(flattened_data, orient='index')

            df.to_csv('tiktokdata.csv', index=False)
        
    # Run the function to get hashtag videos
    asyncio.run(get_hashtag_videos(hashtag))

if __name__ == '__main__':
    get_data(sys.argv[1])
