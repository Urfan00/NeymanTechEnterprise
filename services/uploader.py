

class Uploader:


    # BLOG IMAGES
    @staticmethod
    def blog_images_original(instance, filename):
        return f"Original-Image/Blog/{instance.blog_category.blog_category_title}/{instance.title}/{filename}"

    @staticmethod
    def blog_images_compress(instance, filename):
        return f"Compress-Image/Blog/{instance.blog_category.blog_category_title}/{instance.title}/{filename}"

    # PARTNER IMAGES
    @staticmethod
    def partner_logo_original(instance, filename):
        return f"Original-Image/Partner/{instance.partner_name}/{filename}"

    @staticmethod
    def partner_logo_compress(instance, filename):
        return f"Compress-Image/Partner/{instance.partner_name}/{filename}"

    # SERVICE ICONS
    @staticmethod
    def service_icon_original(instance, filename):
        return f"Original-Image/Service/{instance.service_title}/{filename}"

    @staticmethod
    def service_icon_compress(instance, filename):
        return f"Compress-Image/Service/{instance.service_title}/{filename}"

    # PROJECT IMAGES
    @staticmethod
    def project_image_original(instance, filename):
        return f"Original-Image/Service/{instance.service.service_title}/Project-Image/{instance.project_title}/{filename}"

    @staticmethod
    def project_image_compress(instance, filename):
        return f"Compress-Image/Service/{instance.service.service_title}/Project-Image/{instance.project_title}/{filename}"

    # PROJECT ALL IMAGES
    @staticmethod
    def project_all_images_original(instance, filename):
        return f"Original-Image/Service/{instance.project.service.service_title}/Project-Image/{instance.project.project_title}/ALL-Images/{filename}"

    @staticmethod
    def project_all_images_compress(instance, filename):
        return f"Compress-Image/Service/{instance.project.service.service_title}/Project-Image/{instance.project.project_title}/ALL-Images/{filename}"


