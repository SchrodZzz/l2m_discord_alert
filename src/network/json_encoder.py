class JSONEncoder:

    @staticmethod
    def build_discord_msg_image(text: str, image_url: str):
        json = {
            'content': text,
            'embeds': [
                {
                    'image': {'url': image_url},
                    'height': 300,
                    'width': 300
                }
            ]
        }
        return json

    @staticmethod
    def build_discord_msg_blocks(text: str, first_title: str, first_subtitle: str, second_title: str, second_subtitle):
        json = {
            'content': text,
            'embeds': [
                {'title': first_title, 'description': first_subtitle},
                {'title': second_title, 'description': second_subtitle}
            ]
        }
        return json
