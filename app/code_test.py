@admin.register(Operation)
class OperationAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super().__init__(model, admin_site)

    # Bouton pour exporter en Excel
    @button(label="Exporter en Excel", html_attrs={'style': 'background-color:#00AA00;color:black'})
    def export_to_excel(self, request):
        # Chemin du fichier Excel
        file_path = os.path.join(settings.BASE_DIR, "file_folder/AOO-Guide contrôle a posteriori procédures cLassiques.xlsx")

        try:
            # Essayer d'ouvrir le fichier Excel
            workbook = openpyxl.load_workbook(file_path)
        except FileNotFoundError:
            return HttpResponse("Fichier Excel inexistant.", status=404)        
        
        sheet = workbook["GUIDE_PC_AOO"]  # Sélectionne la première feuille
        
        # Récupérer toutes les données du modèle
        queryset = Operation.objects.all()

        # Récupérer les champs du modèle (en excluant les champs spécifiques comme ForeignKey)
        fields = [field.name for field in Operation._meta.get_fields() if not field.is_relation]      
        
        start_row = 7
        start_col = 1  # Colonne B
            # Insérer les données dans Excel
        for row_num, obj in enumerate(queryset, start=start_row):
            for col_num, field_name in enumerate(fields, start=start_col):
                # Utiliser getattr pour obtenir la valeur du champ
                sheet.cell(row=row_num, column=col_num, value=getattr(obj, field_name))

        # Créer une réponse HTTP pour envoyer le fichier Excel
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=aoo.xlsx'

        # Sauvegarder le fichier Excel dans la réponse
        workbook.save(response)
            
        return response
    





    # Bouton pour exporter en Excel
    # @button(label="Exporter en Excel", html_attrs={'style': 'background-color:#00AA00;color:black'})
    # def export_to_excel(self, request):
    #     workbook = data_to_excel_file("AOO-Guide contrôle a posteriori procédures cLassiques.xlsx", "GUIDE_PC_AOO_VF", 7, 1, 'Aoo')
    #     # Créer une réponse HTTP pour envoyer le fichier Excel
    #     response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    #     response['Content-Disposition'] = 'attachment; filename=Appel_offre_restreint.xlsx'

    #     # Sauvegarder le fichier Excel dans la réponse
    #     workbook.save(response)
    #     return response



    def get_model_by_name(model_name):
    for app_config in apps.get_app_configs():  # Iterate over all apps
        try:
            # Try to get the model from each app's models
            model = apps.get_model(app_config.label, model_name)
            return model
        except LookupError:
            # If model is not found in the current app, continue to the next app
            continue
    print(f"Model '{model_name}' not found in any app.")
    return None


def data_to_excel_file(file, sheet, row, col, model_name):
    # Chemin du fichier Excel
    file_path = os.path.join(settings.FILE_FOLDER, file)
    try:
        # Essayer d'ouvrir le fichier Excel
        workbook = openpyxl.load_workbook(file_path)
    except FileNotFoundError:
        return HttpResponse("Fichier Excel inexistant.", status=404)        
        
    sheet = workbook[sheet]  # Sélectionne la première feuille    
    # Récupérer toutes les données du modèle

    model = get_model_by_name(model_name)

    queryset = model.objects.all()

    # Récupérer les champs du modèle (en excluant les champs spécifiques comme ForeignKey)
    fields = [field.name for field in model._meta.get_fields() if not field.is_relation]      
    
    # Insérer les données dans Excel
    for row_num, obj in enumerate(queryset, start=row):
        for col_num, field_name in enumerate(fields, start=col):
            # Utiliser getattr pour obtenir la valeur du champ
            sheet.cell(row=row_num, column=col_num, value=getattr(obj, field_name))    
    print(workbook)
    return workbook
