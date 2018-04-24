from django.core.exceptions import ObjectDoesNotExist


class AbstractDbIO:
    def __init__(self, model_name):
        self.model = model

    def get_object(self, kwargs):
        """
        get the object using this method
        """
        try:
            return self.model.objects.get(**kwargs)
        except ObjectDoesNotExist:
            return None

    def update_object(self, model_obj, kwargs):
        for key, value in kwargs.items():
            setattr(model_obj, key, value)
        return model_obj.save()

    def create_object(self, kwargs):
        return self.model.save()
