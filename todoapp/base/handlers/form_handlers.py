class FormHandler:
    def load_initials(self, form_class, db_data):
        """
        Method to load inital datasets from the database
        """
        if db_data is None:
            return form_class
        return form_class(initial=db_data.__dict__)
