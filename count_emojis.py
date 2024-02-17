import emoji

def count_emojis(input_str):
    emoji_counts = {}
    
    for char in input_str:
        if char in emoji.UNICODE_EMOJI['en']:
            if char in emoji_counts:
                emoji_counts[char] += 1
            else:
                emoji_counts[char] = 1

    for emoji_char, count in emoji_counts.items():
        print(f"{emoji_char}: {count}")

input_string = '😆😁🔥😝😂😍🎉😊👍😎🎈🥳'

count_emojis(input_string)
