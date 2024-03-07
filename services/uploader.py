

class Uploader:

    @staticmethod
    def blog_images_original(instance, filename):
        return f"Original-Image/Blog/{instance.title}/{filename}"

    @staticmethod
    def blog_images_compress(instance, filename):
        return f"Compress-Image/Blog/{instance.title}/{filename}"

    @staticmethod
    def partner_logo_original(instance, filename):
        return f"Original-Image/Partner/{instance.partner_name}/{filename}"

    @staticmethod
    def partner_logo_compress(instance, filename):
        return f"Compress-Image/Partner/{instance.partner_name}/{filename}"

