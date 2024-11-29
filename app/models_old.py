from django.db import models

class Psd(models.Model):
    # choix
    NATURE_OPERATION = [
        ('Travaux', 'Travaux'),
        ('Fourniture', 'Fourniture'),
        ('Prestation', 'Prestation'),
    ]

    OUI_NON = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
    ]

    # Généralités
    agent_cont = models.CharField(max_length=255, verbose_name="Contrôleur Nom de l'Agent DGMP")
    date_contr = models.DateField(verbose_name="Date de contrôle")
    ministere = models.CharField(max_length=255, verbose_name="Ministère")
    ac = models.CharField(max_length=255, verbose_name="Autorité Contractante")
    pers_res = models.CharField(max_length=255, verbose_name="Personne Ressource Interlocuteur chez l'AC")
    imputation = models.CharField(max_length=255, verbose_name="Imputation Budgétaire")
    # num_ope = models.CharField(max_length=255, verbose_name="Numéro de l’opération (N° formulaire de demande de cotation)")
    objet = models.CharField(max_length=255, verbose_name="Objet de l’opération")
    nat_oper = models.CharField(max_length=255, choices=NATURE_OPERATION, verbose_name="Nature de l’opération")
    nat_oper_obs = models.TextField(verbose_name="Nature de l’opération Observations")

    # Montant de la dotation / ou du Crédit 
    mt_dot = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Montant")
    
    # Situation d'exécution de la ligne budgetaire avant passation
    st_exec_avt_pass_mt = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Montant disponible")
    
    # PSPM
    pspm_exist = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence du PSPM")
    
    # Publication du PSPM
    pub_pspm_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Publication du PPM/PSPM")
    pub_pspm_obs = models.TextField(verbose_name="Observations")
    
    # Inscription de l’opération au PSPM et respect du PSPM
    ope_insc_pspm = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Opération inscrite au PSPM ")
    ope_insc_pspm_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Montant de l'estimation
    mt_est = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Montant")

    # Opération réservée aux PME
    ope_res_pme = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    ope_res_pme_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Date de commande
    dte_commande = models.DateField(verbose_name="Date")
    dte_commande_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Attributaire(s)
    att_rs_soc = models.CharField(max_length=255, null=True, blank=True, verbose_name="Raison sociale")
    att_ncc_att = models.CharField(max_length=255, null=True, blank=True, verbose_name="NCC attributaire")
    att_mt = models.CharField(max_length=255, null=True, blank=True, verbose_name="Montant")
    att_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Ecart entre montant estimatif et montant attribué
    ect_mte_mta = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Montant")

    EXHAUSTIVITE = [
        ('Complet', 'Complet'),
        ('Incomplet', 'Incomplet')
    ]

    # Existence et exhaustivité de l'archivage des documents
    ext_exh_arch_doc_exi = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence")
    ext_exh_arch_doc_exh = models.CharField(max_length=9, choices=EXHAUSTIVITE, verbose_name="Exhaustivité")
    ext_exh_arch_doc_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    class Meta:
        verbose_name = "PSD"
        verbose_name_plural = "PSD"
    
    def __str__(self):
        return f"Opération {self.num_ope} - {self.objet} - {self.ministere} - {self.ac}"
    

