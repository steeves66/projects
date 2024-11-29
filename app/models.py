from django.db import models
from django.core.validators import MinValueValidator

class Aoo(models.Model):
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
    num_aoo = models.CharField(max_length=255, verbose_name="Numéro de l’opération No de l'AOO")
    objet = models.CharField(max_length=255, verbose_name="Objet de l’opération")
    nat_oper = models.CharField(max_length=255, 
                                choices=NATURE_OPERATION,
                                verbose_name="Nature de l’opération Travaux/Fournitures/Prestations")
    nat_oper_obs = models.TextField(verbose_name="Nature de l’opération Observations", null=True, blank=True)

    # PPM
    ppm_exist = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence du PPM")
    ppm_obs = models.TextField(verbose_name="PPM Observations", null=True, blank=True)
    # Publication du PPM
    pub_ppm_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Publication du PPM existence")
    pub_ppm_obs = models.TextField(verbose_name="Publication du PPM Observations", null=True, blank=True)
    # Inscription de l’opération au PPM
    ope_insc_ppm = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Opération inscrite au PPM")
    ope_insc_ppm_obs = models.TextField(verbose_name="Observations", null=True, blank=True)


    mt_dot = models.BigIntegerField(verbose_name="Montant de la dotation / du Crédit", validators=[MinValueValidator(0)])
    st_exec_avt_pass_mt = models.BigIntegerField(verbose_name="Situation d’exécution de la ligne budgétaire avant passation")
    mt_est = models.BigIntegerField(verbose_name="Montant de l'estimation", validators=[MinValueValidator(0)])

    # Opération réservée aux PME
    ope_res_pme = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Opération réservée aux PME")
    ope_res_pme_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Examen et validation du DAO par la DGMP 
    exam_val_dao_dgmp_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    exam_val_dao_dgmp_dte_dao_dgmp = models.DateField(verbose_name="Date de réception du DAO", null=True, blank=True)
    exam_val_dao_dgmp_dte_dao_dgmp_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Exigence du quitus de non redevance dans le DAO 
    exg_quitus_dao_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Exigence du quitus de non redevance dans le DAO")
    exg_quitus_dao_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Garantie de l'offre comprise entre 1 et 1,5%
    gar_offre_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Garantie de l'offre comprise entre 1 et 1,5%")
    gar_offre_cst_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Publication de l'avis d'appel d'offres dans le BOMP
    pub_aao_bomp_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence de la publication dans le BOMP")
    pub_aao_bomp_date = models.DateField(verbose_name="Date de publication dans le BOMP", null=True, blank=True)
    pub_aao_bomp_no_bomp = models.CharField(max_length=10, verbose_name="Numéro du BOMP")
    pub_aao_bomp_duree = models.BigIntegerField(verbose_name="Durée de publication", null=True, blank=True)
    pub_aao_bomp_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Existence d’une liste de retrait du DAO
    exist_lst_rtr_dao_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat", null=True, blank=True)
    exist_lst_rtr_dao_nb_dos_ret = models.BigIntegerField(verbose_name="Nombre de dossiers rétirés", null=True, blank=True)
    exist_lst_rtr_dao_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Convocation de la COJO
    conv_cojo_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat", null=True, blank=True)
    conv_cojo_obs = models.TextField(verbose_name="Convocation de la COJO Observations", null=True, blank=True)

    # Existence de la COJO
    exist_cojo_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence de la COJO Constat",  null=True, blank=True)
    exist_cojo_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Composition de la COJO
    comp_cojo_conf = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Conforme", null=True, blank=True)
    comp_cojo_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Existence d’une liste de présence des membres de la COJO
    exist_lst_prs_mb_cojo_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    exist_lst_prs_mb_cojo_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
   
    # Existence des mandats  des répresentants des membres de la COJO
    exist_mdt_rep_mb_cojo_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    exist_mdt_rep_mb_cojo_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Respect du quorum au niveau de la COJO
    res_qr_nv_cojo_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    res_qr_nv_cojo_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Existence d’une liste de dépôt des plis
    exist_lst_dpt_plis_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    exist_lst_dpt_plis_nb_plis_dep = models.BigIntegerField(verbose_name="Nombre de plis déposés", null=True, blank=True)
    exist_lst_dpt_plis_conf_lst_dpt_lst_rtr = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Conformité de la liste de dépôt avec la liste de retrait")
    exist_lst_dpt_plis_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Respect des date et heure limites de dépôt des plis 
    resp_date_heure_lmt_dep_plis_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    resp_date_heure_lmt_dep_plis_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Respect des date et heure d'ouverture des plis
    resp_date_heure_lmt_ouv_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    resp_date_heure_lmt_ouv_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Existence d’une liste de présence des soumissionnaires
    ext_lst_prsc_sum_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    ext_lst_prsc_sum_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Existence du procès-verbal d’ouverture des plis
    ext_pv_ouv_plis = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence du PV ouverture des plis")
    ext_pv_ouv_plis_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Existence du rapport d’analyse des offres
    ext_rap_ana = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence du rapport")
    ext_rap_ana_obs = models.TextField(verbose_name="observation", null=True, blank=True)
    
    # Conformité de la COJO au jugement
    conf_cojo_jug_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat", null=True, blank=True)
    conf_cojo_jug_obs = models.TextField(verbose_name="Conformité de la COJO au jugement Observations", null=True, blank=True)
    
    # Existence du procès-verbal de jugement des offres
    ext_pv_jug_off_exst_pv = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence du PV",  null=True, blank=True)
    ext_pv_jug_off_exst_pv_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
     
    # Respect du délai imparti à la COJO pour ses travaux
    resp_del_imp_cojo_trv_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    resp_del_imp_cojo_trv_dta_ouv = models.DateField(verbose_name="Date d'ouverture", null=True, blank=True)
    resp_del_imp_cojo_trv_dta_jug = models.DateField(null=True, blank=True, verbose_name="Date de jugement")
    resp_del_imp_cojo_trv_dta_dern_jug = models.DateField(null=True, blank=True, verbose_name="Date du dernier jugement")
    resp_del_imp_cojo_trv_nb_jug = models.BigIntegerField(null=True, blank=True, verbose_name="Nombre de jugements", validators=[MinValueValidator(0)])
    resp_del_imp_cojo_trv_del_trv = models.BigIntegerField(null=True, blank=True, verbose_name="Delai des travaux (en jours ouvrables)")
    resp_del_imp_cojo_trv_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Publication des résultats de la COJO par la DGMP
    pub_res_cojo_dgmp_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Publication des résultats de la COJO par la DGMP Constat")
    pub_res_cojo_dgmp_date_pub = models.DateField(null=True, blank=True, verbose_name="Date de publication")
    pub_res_cojo_dgmp_no_bomp = models.CharField(max_length=255, null=True, blank=True, verbose_name="Numéro BOMP")
    pub_res_cojo_dgmp_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Notification des résultats aux attributaires
    not_res_att_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    not_res_att_date = models.DateField(null=True, blank=True, verbose_name="Date")
    not_res_att_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    SOUMISSIONNAIRE_NON_RETENU = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
        ('Partiel', 'Partiel'),
    ]

    # Information des soumissionnaires non retenus sur les résultats
    inf_soum_nn_ret_res_cst = models.CharField(max_length=7, choices=SOUMISSIONNAIRE_NON_RETENU, verbose_name="Constat")
    inf_soum_nn_ret_res_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Attributaire(s)
    att_rs_soc = models.CharField(max_length=255, null=True, blank=True, verbose_name="Raison sociale")
    att_ncc_att = models.CharField(max_length=255, null=True, blank=True, verbose_name="NCC attributaire")
    att_lot = models.CharField(max_length=255, null=True, blank=True, verbose_name="Lot")
    att_mt = models.BigIntegerField(verbose_name="Montant", null=True, blank=True)
    att_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Respect du délai de recours éventuel
    res_del_rec_evt_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    res_del_rec_evt_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Restitution des actes de garantie aux soumissionnaires non retenus
    rst_act_gar_soum_nn_ret_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    rst_act_gar_soum_nn_ret_rspt_del_rst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Respect du delai de restitution")
    rst_act_gar_soum_nn_ret_rspt_del_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Existence un marché
    ext_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    ext_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Conformité du contenu du marché
    conf_cont_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    conf_cont_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Signature du marché par attributaire
    sig_mar_att_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    sig_mar_att_date = models.DateField(null=True, blank=True, verbose_name="Date de signature")
    sig_mar_att_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Signature du marché par Autorité Contractante
    sig_mar_ac_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    sig_mar_ac_date = models.DateField(null=True, blank=True, verbose_name="Date de signature")
    sig_mar_ac_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Signature de l'Autorité compétente
    sig_aco_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    sig_aco_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Numérotation du marché
    num_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    num_mar_date_num = models.DateField(null=True, blank=True, verbose_name="Date de Numérotation")
    num_mar_nom = models.CharField(max_length=255, null=True, blank=True, verbose_name="Numéro du mrché")
    num_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Conformité du Numéro du marché
    conf_num_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Conformité du Numéro du marche Constat")
    conf_num_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Montant du marché
    mt_mar = models.BigIntegerField(null=True, blank=True, verbose_name="Montant", validators=[MinValueValidator(0)])
   
    # Ecart entre montant estimatif et montant attribué
    ect_mte_mta = models.BigIntegerField(null=True, blank=True, verbose_name="Montant", validators=[MinValueValidator(0)])

    # Production des pièces fiscales et sociales par attributaire
    prd_pc_fic_soc_att_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    prd_pc_fic_soc_att_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Examen préalable à l'approbation
    exm_pre_app_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    exm_pre_app_dte_trm_prjm_dgmp = models.DateField(null=True, blank=True, verbose_name="Date de transmission ou de soumission du projet de marche à la DGMP")
    exm_pre_app_dte_trm_rslt_exm_dgmp_ac = models.DateField(null=True, blank=True, verbose_name="Date de transmission du résultat de l'examen par la DGMP à l'AC")
    exm_pre_app_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Approbation du marché
    app_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    app_mar_date = models.DateField(null=True, blank=True, verbose_name="Date d'approbation")
    app_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Autorité approbatrice ou organe approbateur compétent
    aut_app_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    aut_app_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Notification de l'approbation du marché au titulaire
    not_app_mar_ttl = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    not_app_mar_ttl_date_rec = models.DateField(null=True, blank=True, verbose_name="Date de réception par le titulaire")
    not_app_mar_ttl_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Enregistrement du marché
    enr_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    enr_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Transmission de 02 exemplaires du contrat à la DGMP
    trans_dx_exp_ctr_dgmp_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Transmission de 02 exemplaires du contrat à la DGMP Constat")
    trans_dx_exp_ctr_dgmp_obs = models.TextField(null=True, blank=True, verbose_name="Transmission de 02 exemplaires du contrat à la DGMP Observations")

    # Notification de l'ordre de service de démarrage
    not_osd_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    not_osd_date_accr = models.DateField(null=True, blank=True, verbose_name="Date sur l'accusé de réception")
    not_osd_conf = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Conformité de la notification")
    not_osd_obs = models.TextField(null=True, blank=True, verbose_name="Observations")


    EXHAUSTIVITE = [
        ('Complet', 'Complet'),
        ('Incomplet', 'Incomplet')
    ]

    # Existence et exhaustivité de l'archivage des documents
    ext_exh_arch_doc_exi = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence")
    ext_exh_arch_doc_exh = models.CharField(choices=EXHAUSTIVITE, verbose_name="Exhaustivité", max_length=20, null=True, blank=True)
    ext_exh_arch_doc_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Temps total pour la conduite de l’opération
    tps_tt_cdt_ope_nb_jrs = models.BigIntegerField(null=True, blank=True, verbose_name="Nombre de jours")
    tps_tt_cdt_ope_nb_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    class Meta:
        verbose_name = "AOO"
        verbose_name_plural = "AOO"
    
    def __str__(self):
        return f"Opération {self.num_aoo} - {self.objet} - {self.ministere} - {self.ac}"
    

class Aor(models.Model):
    OUI_NON = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
    ]

    # Nature de l'opération
    NATURE_OPERATION = [
        ('travaux', 'Travaux'),
        ('fournitures', 'Fournitures'),
        ('prestations', 'Prestations'),
    ]

    # Informations générales
    agent_cont = models.CharField(max_length=255, verbose_name="Contrôleur")
    date_contr = models.DateField(verbose_name="Date de contrôle")
    ministere = models.CharField(max_length=255, verbose_name="Ministère")
    ac = models.CharField(max_length=255, verbose_name="Autorité Contractante")
    pers_res = models.CharField(max_length=255, verbose_name="Personne Ressource chez l’interlocuteur")
    imputation = models.CharField(max_length=255, verbose_name="Imputation Budgétaire")
    num_aoo = models.CharField(max_length=255, verbose_name="Numéro de l'opération")
    objet = models.TextField(verbose_name="Objet de l'Opération")
    
    # Nature de l'opération
    nat_oper = models.CharField(max_length=11, choices=NATURE_OPERATION, verbose_name="Nature de l'opération")
    nat_oper_obs = models.TextField(blank=True, null=True, verbose_name="Nature de l'opération observation")
    
    # PPM / PSPM
    ppm_exist = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence du PPM / PSPM")

    # Publication du PPM
    pub_ppm_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Publication du PPM/PSPM")
    pub_ppm_obs = models.TextField(blank=True, null=True, verbose_name="Observations")
    
    # Inscription de l’opération au PPM / PSPM et respect du PPM / PSPM
    ope_insc_ppm = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Opération inscrite au PPM / PSPM")
    ope_insc_ppm_obs = models.TextField(blank=True, null=True, verbose_name="Observations")
    
    # Montant de la dotation / du Crédit 
    mt_dot = models.PositiveBigIntegerField(verbose_name="Montant de la dotation / du Crédit")

    # Situation d'exécution de la ligne budgetaire avant passation
    st_exec_avt_pass_mt_disp = models.CharField(max_length=255, blank=True, null=True, verbose_name="Montant Disponible")

    # Montant de l'estimation
    mt_est = models.PositiveBigIntegerField(verbose_name="Montant de l'estimation")
    
    # Opération réservée aux PME
    ope_res_pme = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    ope_res_pme_obs = models.TextField(blank=True, null=True, verbose_name="Observations")
    
    # Mode de sélection des entreprises
    MOD_SEL_ENT_CHOICES = [
        ('AMI', 'AMI'),
        ('AOR', 'Liste Restreinte Autorisée'),
    ]
    mod_sel_ent = models.CharField(max_length=50, choices=MOD_SEL_ENT_CHOICES, verbose_name="Mode de sélection des entreprises")
    
    # Publication de l'avis de préqualification ou de l'AMI dans le BOMP et sur le site de la DGMP
    pub_adp_ami_bomp_int_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    pub_adp_ami_bomp_int_date = models.DateField(blank=True, null=True, verbose_name="Date de publication")
    pub_adp_ami_bomp_int_obs = models.TextField(blank=True, null=True, verbose_name="Observations")
    
    # Lettre d'invitation de l'AC aux entreprises (AOR)
    lt_inv_ac_ent_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    lt_inv_ac_ent_nb = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Nombre d'entreprises invitées", validators=[MinValueValidator(0)])
    
    # Accord de participation des candidats sollicités (AOR)
    acd_part_cand_sol_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    acd_part_cand_sol_obs = models.TextField(blank=True, null=True, verbose_name="Observations")
    
    # Autorisation de recourir à l'AOR  
    aut_rec_aor_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    aut_rec_aor_ref = models.CharField(max_length=255, blank=True, null=True, verbose_name="Référence de l'autorisation")

    # Liste des entreprises autorisées à participer à la concurrence 
    ent_1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Entreprise 1")
    ent_2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Entreprise 2")
    ent_3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Entreprise 3")
    ent_4 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Entreprise 4")
    ent_5 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Entreprise 5")

    # Examen DAO / DP à la DGMP
    exm_val_dao_dp_dgmp_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    exm_val_dao_dp_dgmp_date = models.DateField(blank=True, null=True, verbose_name="Date de réception DAO/DP à la DGMP")
    exm_val_dao_dp_dgmp_obs = models.TextField(blank=True, null=True, verbose_name="Observations")
    
    # Exigence du quitus de non redevance dans le DAO 
    exg_quitus_dao_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    exg_quitus_dao_obs = models.TextField(blank=True, null=True, verbose_name="Observations")
    
    # Garantie de l'offre comprise entre 1 et 1,5%
    gar_offre_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    gar_offre_cst_obs = models.TextField(blank=True, null=True, verbose_name="Observations")
    
    # Transmission des lettres d'invitation aux candidats autorisés à participer à la concurrence
    trm_let_inv_cnd_aut_prt_ccr_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat", blank=True, null=True)
    trm_let_inv_cnd_aut_prt_ccr_date = models.DateField(blank=True, null=True, verbose_name="Date de transmission")
    trm_let_inv_cnd_aut_prt_ccr_obs = models.TextField(blank=True, null=True, verbose_name="Observations")
    
    # Convocation COJO
    conv_cojo_cst = models.CharField(max_length=3, choices=OUI_NON, blank=True, null=True, verbose_name="Constat")
    conv_cojo_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Existence de la COJO
    exist_cojo_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    exist_cojo_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Composition de la COJO
    comp_cojo_conf = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Conformité du COJO")
    comp_cojo_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Existence d’une liste de présence des membres de la COJO
    exist_lst_prs_mb_cojo_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    exist_lst_prs_mb_cojo_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Existence des mandats des répresentants des membres de la COJO
    exist_mdt_rep_mb_cojo_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    exist_mdt_rep_mb_cojo_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Respect du quorum au niveau de la COJO
    res_qr_nv_cojo_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    res_qr_nv_cojo_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Existence d’une liste de dépôt des plis
    exist_lst_dpt_plis_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    exist_lst_dpt_plis_nb_plis_dep = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Nombre de plis déposés")
    exist_lst_dpt_plis_conf_lst_dpt_lst_rtr = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Conformité de la liste de dépôt avec la liste de retrait")
    exist_lst_dpt_plis_obs = models.TextField(blank=True, null=True, verbose_name="Observations")
    
    # Respect des date et heure limites de dépôt des plis
    resp_date_heure_lmt_dep_plis_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    resp_date_heure_lmt_dep_plis_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Respect des date et heure d'ouverture des plis
    resp_date_heure_lmt_ouv_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    resp_date_heure_lmt_ouv_obs = models.TextField(blank=True, null=True, verbose_name="Observations")
    
    # Nombre de plis reçus à l'ouverture
    nb_plis_rec_ouv_dep = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Nombre de plis déposés")
    nb_plis_rec_ouv_obs = models.TextField(blank=True, null=True, verbose_name="Observations")
    
    # Existence d’une liste de présence des soumissionnaires
    ext_lst_prsc_sum_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    ext_lst_prsc_sum_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Existence du procès-verbal d’ouverture des plis
    ext_pv_ouv_plis = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence du PV d'ouverture")
    ext_pv_ouv_plis_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Existence du rapport d’analyse des offres
    ext_rap_ana = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence du rapport d'analyse")
    ext_rap_ana_obs = models.TextField(blank=True, null=True, verbose_name="Observations")
    
    # Conformité de la COJO au jugement
    conf_cojo_jug_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    conf_cojo_jug_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Existence du procès-verbal de jugement des offres
    ext_pv_jug_off_exst_pv = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence du PV")
    ext_pv_jug_off_exst_pv_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Respect du délai imparti à la COJO pour ses travaux
    resp_del_imp_cojo_trv_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Responsabilité du COJO")
    resp_del_imp_cojo_trv_dta_ouv = models.DateField(blank=True, null=True, verbose_name="Date d'ouverture")
    resp_del_imp_cojo_trv_dta_jug = models.DateField(blank=True, null=True, verbose_name="Date de jugement")
    resp_del_imp_cojo_trv_dta_dern_jug = models.DateField(blank=True, null=True, verbose_name="Date du dernier jugement")
    resp_del_imp_cojo_trv_nb_jug = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Nombre de jugements")
    resp_del_imp_cojo_trv_del_trv = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Délai des travaux (en jours ouvrables)")
    resp_del_imp_cojo_trv_obs = models.TextField(blank=True, null=True, verbose_name="Observations")
    
    #  Publication des résultats de la COJO par la DGMP
    pub_res_cojo_dgmp_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat de publication")
    pub_res_cojo_dgmp_date_pub = models.DateField(blank=True, null=True, verbose_name="Date de publication")
    pub_res_cojo_dgmp_no_bomp = models.TextField(blank=True, null=True, verbose_name="Numéro du BOMP")
    pub_res_cojo_dgmp_obs = models.TextField(blank=True, null=True, verbose_name="Observations")
    
    # Notification des résultats aux attributaires
    not_res_att_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    not_res_att_date = models.DateField(blank=True, null=True, verbose_name="Date de notification")
    not_res_att_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Information des soumissionnaires sur les résultats
    inf_soum_res_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    inf_soum_res_obs = models.TextField(blank=True, null=True, verbose_name="Observations")
    
    # Attributaire
    att_rs_soc = models.TextField(blank=True, null=True, verbose_name="Raison sociale")
    att_ncc_att = models.CharField(max_length=20, blank=True, null=True, verbose_name="NCC attributaire")
    att_lot = models.TextField(blank=True, null=True, verbose_name="Lot")
    att_mt = models.PositiveBigIntegerField(blank=True, null=True, verbose_name="Montant")
    att_obs = models.TextField(blank=True, null=True, verbose_name="Observations")
    
    # Respect du délai de recours éventuels
    res_del_rec_evt_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    res_del_rec_evt_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Restitution des actes de garantie aux soumissionnaires non retenus
    rst_act_gar_soum_nn_ret_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    rst_act_gar_soum_nn_ret_rspt_del_rst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Respect du délai de restitution")
    rst_act_gar_soum_nn_ret_rspt_del_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Existence d’un marché
    ext_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    ext_mar_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Conformité du contenu du marché
    conf_cont_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    conf_cont_mar_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Signature du marché par l’attributaire
    sig_mar_att_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    sig_mar_att_date = models.DateField(blank=True, null=True, verbose_name="Date de signature")
    sig_mar_att_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Signature du marché par l’Autorité Contractante
    sig_mar_ac_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    sig_mar_ac_date = models.DateField(blank=True, null=True, verbose_name="Date de signature")
    sig_mar_ac_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Signature de l’autorité compétente
    sig_aco_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    sig_aco_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Numérotation du marché
    num_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    num_mar_date_num = models.DateField(blank=True, null=True, verbose_name="Date de numérotation")
    num_mar_nom = models.CharField(max_length=255, blank=True, null=True, verbose_name="Numéro")
    num_mar_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Conformité du numéro du marché
    conf_num_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    conf_num_mar_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Montant du marché
    mt_mar = models.PositiveIntegerField(blank=True, null=True, verbose_name="Montant du marché")

    # Ecart entre montant estimatif et montant attribué
    ect_mte_mta = models.PositiveBigIntegerField(blank=True, null=True, verbose_name="Ecart entre montant estimatif et montant attribué")

    # Production des pièces fiscales et sociales par l’attributaire
    prd_pc_fic_soc_att_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    prd_pc_fic_soc_att_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Examen préalable à l'approbation
    exm_pre_app_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    exm_pre_app_dte_trm_prjm_dgmp = models.DateField(blank=True, null=True, verbose_name="Date de transmission ou soumission du projet de marché à la DGMP")
    exm_pre_app_dte_trm_rslt_exm_dgmp_ac = models.DateField(blank=True, null=True, verbose_name="Date de transmission du résultat de l'examen par la DGMP à l'AC")
    exm_pre_app_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Approbation du marché
    app_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    app_mar_date = models.DateField(blank=True, null=True, verbose_name="Date d'approbation")
    app_mar_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Autorité approbatrice ou  organe approbateur compétent
    aut_app_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    aut_app_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Notification de l’approbation du marché au titulaire
    not_app_mar_ttl = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    not_app_mar_ttl_date_rec = models.DateField(blank=True, null=True, verbose_name="Date de réception par le titulaire")
    not_app_mar_ttl_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Enregistrement du marché
    enr_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    enr_mar_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Transmission de 02 exemplaires du contrat à la DGMP
    trans_dx_exp_ctr_dgmp_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    trans_dx_exp_ctr_dgmp_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # Notification de l’ordre de service de démarrage
    not_osd_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    not_osd_date_accr = models.DateField(blank=True, null=True, verbose_name="Date sur l'accusé de réception")
    not_osd_conf = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Conforme")
    not_osd_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    EXHAUSTIVITE = [
        ('Complet', 'Complet'),
        ('Incomplet', 'Incomplet')
    ]
    # Existence et exhaustivité de l’archivage des documents
    ext_exh_arch_doc_exi = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence")
    ext_exh_arch_doc_exh = models.CharField(max_length=9, choices=EXHAUSTIVITE, blank=True, null=True, verbose_name="Exhaustivité")
    ext_exh_arch_doc_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    # tps_tt_cdt_ope_nb_jrs = models.BigIntegerField(blank=True, null=True, verbose_name="Nombre de jours")
    # tps_tt_cdt_ope_nb_obs = models.TextField(blank=True, null=True, verbose_name="Observations")

    class Meta:
        verbose_name = "AOR"
        verbose_name_plural = "AOR"
    
    def __str__(self):
        return f"Opération {self.num_aoo} - {self.objet} - {self.ministere} - {self.ac}"
    

class Gag(models.Model):
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
    objet = models.CharField(max_length=255, verbose_name="Objet de l’opération") 
    nat_oper = models.CharField(max_length=255, choices=NATURE_OPERATION, verbose_name="Nature de l’opération Travaux/Fournitures/Prestations")
    nat_oper_obs = models.TextField(verbose_name="Nature de l’opération Observations")

    # Préparation du PPM
    ppm_exist = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence du PPM") 

    # Publication du PPM
    pub_ppm_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Publication du PPM existence")
    pub_ppm_obs = models.TextField(verbose_name="Publication du PPM Observations")

    # Inscription de l’opération au PPM et respect du PPM
    ope_insc_ppm = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Opération inscrite au PPM")
    ope_insc_ppm_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Montant de la dotation / du Crédit 
    mt_dot = models.PositiveBigIntegerField(verbose_name="Montant de la dotation / du Crédit") 

    # Montant de l'Estimation
    mt_est = models.PositiveBigIntegerField(verbose_name="Montant de l'estimation") 

    # Situation d'exécution de la ligne budgetaire avant passation
    st_exec_avt_pass_mt = models.PositiveBigIntegerField(verbose_name="Situation d’exécution de la ligne budgétaire avant passation") 

    # Opération réservée aux PME
    ope_res_pme = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    ope_res_pme_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # PV de négociation ou de consultation
    pv_neg_consult_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    pv_neg_consult_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Autorisation de recourir au Gré à Gré   
    aut_rec_gag_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    aut_rec_gag_ref = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Référence de l'autorisation")

    # Attributaire(s)
    att_rs_soc = models.CharField(max_length=255, null=True, blank=True, verbose_name="Raison sociale")
    att_ncc_att = models.CharField(max_length=255, null=True, blank=True, verbose_name="NCC attributaire")
    att_lot = models.CharField(max_length=255, null=True, blank=True, verbose_name="Lot")
    att_mt = models.PositiveBigIntegerField(verbose_name="Montant", null=True, blank=True)
    att_obs = models.TextField(null=True, blank=True, verbose_name="Observations")
    
    # Existence un marché
    ext_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    ext_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Conformité du contenu du marché
    conf_cont_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    conf_cont_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Signature du marché par attributaire
    sig_mar_att_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    sig_mar_att_date = models.DateField(null=True, blank=True, verbose_name="Date de signature")
    sig_mar_att_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Signature du marché par Autorité Contractante
    sig_mar_ac_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    sig_mar_ac_date = models.DateField(null=True, blank=True, verbose_name="Date de signature")
    sig_mar_ac_obs = models.TextField(null=True, blank=True, verbose_name="Observations")
    
    # Signature de l'Autorité compétente
    sig_aco_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    sig_aco_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Numérotation du marché
    num_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    num_mar_date_num = models.DateField(null=True, blank=True, verbose_name="Date de Numérotation")
    num_mar_nom = models.CharField(max_length=255, null=True, blank=True, verbose_name="Numéro du mrché")

    # Conformité du Numéro du marché
    conf_num_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Conformité du Numéro du marche Constat")
    conf_num_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Montant du marché
    mt_mar = models.PositiveBigIntegerField(null=True, blank=True, verbose_name="Montant")
    
    # Production des pièces fiscales et sociales par attributaire
    prd_pc_fic_soc_att_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    prd_pc_fic_soc_att_obs = models.TextField(null=True, blank=True, verbose_name="Observations")
    
    # Examen préalable à l'approbation
    exm_pre_app_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    exm_pre_app_dte_trm_prjm_dgmp = models.DateField(null=True, blank=True, verbose_name="Date de transmission ou de soumission du projet de marche à la DGMP")
    exm_pre_app_dte_trm_rslt_exm_dgmp_ac = models.DateField(null=True, blank=True, verbose_name="Date de transmission du résultat de l'examen par la DGMP à l'AC")
    exm_pre_app_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Approbation du marché
    app_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    app_mar_date = models.DateField(null=True, blank=True, verbose_name="Date d'approbation")
    app_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")
    
    # Autorité approbatrice ou organe approbateur compétent
    aut_app_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    aut_app_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Notification de l'approbation du marché au titulaire
    not_app_mar_ttl = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    not_app_mar_ttl_date_rec = models.DateField(null=True, blank=True, verbose_name="Date de réception par le titulaire")
    not_app_mar_ttl_obs = models.TextField(null=True, blank=True, verbose_name="Observations")
    
    # Enregistrement du marché
    enr_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    enr_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Notification de l'ordre de service de démarrage
    not_osd_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    not_osd_date_accr = models.DateField(null=True, blank=True, verbose_name="Date sur l'accusé de réception")
    not_osd_conf = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Conformité de la notification")
    not_osd_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    EXHAUSTIVITE = [
        ('Complet', 'Complet'),
        ('Incomplet', 'Incomplet')
    ]

    # Existence et exhaustivité de l'archivage des documents
    ext_exh_arch_doc_exi = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence")
    ext_exh_arch_doc_exh = models.CharField(choices=EXHAUSTIVITE, verbose_name="Exhaustivité", max_length=20, null=True, blank=True)
    ext_exh_arch_doc_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    class Meta:
        verbose_name = "GAG"
        verbose_name_plural = "GAG"
        
    def __str__(self):
        return f"Opération {self.objet} - {self.ministere} - {self.ac}"


class Pso(models.Model):
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
    num_aoo = models.CharField(max_length=255, verbose_name="Numéro de l’opération No de l'AO")
    objet = models.CharField(max_length=255, verbose_name="Objet de l’opération")
    nat_oper = models.CharField(max_length=255, choices=NATURE_OPERATION, verbose_name="Nature de l’opération")
    nat_oper_obs = models.TextField(verbose_name="Nature de l’opération Observations", null=True, blank=True)

    # PSPM
    pspm_exist = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence du PSPM")

    # Publication du PSPM
    pub_pspm_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    pub_pspm_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Inscription de l’opération au PSPM et respect du PSPM
    ope_insc_pspm = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Opération inscrite au PSPM ")
    ope_insc_pspm_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Montant de la dotation / du Crédit 
    mt_dot = models.PositiveBigIntegerField(verbose_name="Montant")
    
    # Situation d'exécution de la ligne budgetaire avant passation
    st_exec_avt_pass_mt = models.PositiveBigIntegerField(verbose_name="Montant disponible")
    
    # Montant de l'estimation
    mt_est = models.PositiveBigIntegerField(verbose_name="Montant")

    # Opération réservée aux PME
    ope_res_pme = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    ope_res_pme_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Examen et validation du DAO par la DGMP 
    exam_val_dao_dgmp_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat", null=True, blank=True)
    exam_val_dao_dgmp_dte_dao_dgmp = models.DateField(verbose_name="Date de réception du DAO", null=True, blank=True)
    exam_val_dao_dgmp_dte_dao_dgmp_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Exigence du quitus de non redevance dans le DAO 
    exg_quitus_dao_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    exg_quitus_dao_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Publication de l'avis d'appel d'offres dans le BOMP
    pub_aao_bomp_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    pub_aao_bomp_date = models.DateField(verbose_name="Date de publication", null=True, blank=True)
    pub_aao_bomp_no_bomp = models.BigIntegerField(verbose_name="Numéro du BOMP")
    pub_aao_bomp_duree = models.BigIntegerField(verbose_name="Durée de publication", null=True, blank=True)
    pub_aao_bomp_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Existence d’une liste de retrait du dossier de consultation 
    exist_lst_rtr_dao_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat", null=True, blank=True)
    exist_lst_rtr_dao_nb_dos_ret = models.PositiveSmallIntegerField(verbose_name="Nombre de dossiers rétirés", null=True, blank=True)
    exist_lst_rtr_dao_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Convocation de la COPE
    conv_cojo_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat", null=True, blank=True)
    conv_cojo_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Existence de la COPE
    exist_cojo_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    exist_cojo_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Composition de la COPE
    comp_cojo_conf = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat", null=True, blank=True)
    comp_cojo_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Existence d’une liste de présence des membres de la COPE
    exist_lst_prs_mb_cojo_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    exist_lst_prs_mb_cojo_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
   
    # Existence des mandats des répresentants des membres de la COPE
    exist_mdt_rep_mb_cojo_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    exist_mdt_rep_mb_cojo_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Respect du quorum au niveau de la COPE
    res_qr_nv_cojo_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    res_qr_nv_cojo_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Existence d’une liste de dépôt des plis
    exist_lst_dpt_plis_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    exist_lst_dpt_plis_nb_plis_dep = models.PositiveSmallIntegerField(verbose_name="Nombre de plis déposés", null=True, blank=True)
    exist_lst_dpt_plis_conf_lst_dpt_lst_rtr = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Conformité de la liste de dépôt avec la liste de retrait")
    exist_lst_dpt_plis_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Respect des dates et heures limites de dépôt des plis 
    resp_date_heure_lmt_dep_plis_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    resp_date_heure_lmt_dep_plis_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Respect des dates et heures d'ouverture des plis
    resp_date_heure_lmt_ouv_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    resp_date_heure_lmt_ouv_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Existence d’une liste de présence des soumissionnaires
    ext_lst_prsc_sum_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    ext_lst_prsc_sum_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Existence du procès-verbal d’ouverture des plis
    ext_pv_ouv_plis = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    ext_pv_ouv_plis_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Existence et conformité du rapport d’analyse des offres
    ext_rap_ana = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence du rapport")
    ext_rap_ana_obs = models.TextField(verbose_name="observation", null=True, blank=True)
    
    # Conformité de la COPE au jugement
    conf_cojo_jug_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    conf_cojo_jug_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Existence du procès-verbal de jugement des offres
    ext_pv_jug_off_exst_pv = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence du procès-verbal de jugement")
    ext_pv_jug_off_exst_pv_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
     
    # Respect du délai imparti à la COPE pour ses travaux
    resp_del_imp_cojo_trv_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    resp_del_imp_cojo_trv_dta_ouv = models.DateField(verbose_name="Date d'ouverture", null=True, blank=True)
    resp_del_imp_cojo_trv_dta_jug = models.DateField(null=True, blank=True, verbose_name="Date de jugement")
    resp_del_imp_cojo_trv_dta_dern_jug = models.DateField(null=True, blank=True, verbose_name="Date du dernier jugement")
    resp_del_imp_cojo_trv_nb_jug = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Nombre de jugements")
    resp_del_imp_cojo_trv_del_trv = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Delai des travaux (en jours ouvrables)")
    resp_del_imp_cojo_trv_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Publication des résultats de la COPE par la DGMP
    pub_res_cojo_dgmp_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    pub_res_cojo_dgmp_date_pub = models.DateField(null=True, blank=True, verbose_name="Date de publication")
    pub_res_cojo_dgmp_no_bomp = models.CharField(max_length=255, null=True, blank=True, verbose_name="Numéro BOMP")
    pub_res_cojo_dgmp_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Notification des résultats aux attributaires
    not_res_att_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    not_res_att_date = models.DateField(null=True, blank=True, verbose_name="Date")
    not_res_att_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Information des soumissionnaires non retenus
    inf_soum_nn_ret_res_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    inf_soum_nn_ret_res_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Attributaire(s)
    att_rs_soc = models.CharField(max_length=255, null=True, blank=True, verbose_name="Raison sociale")
    att_ncc_att = models.CharField(max_length=255, null=True, blank=True, verbose_name="NCC attributaire")
    att_lot = models.CharField(max_length=255, null=True, blank=True, verbose_name="Lot")
    att_mt = models.PositiveBigIntegerField(verbose_name="Montant", null=True, blank=True)
    att_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Respect du délai de recours éventuel
    res_del_rec_evt_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Respect du délai de recours éventuels Constat")
    res_del_rec_evt_nb_rec =  models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Nombre de recours")
    res_del_rec_evt_obs = models.TextField(null=True, blank=True, verbose_name="Respect du délai de recours éventuels Observations")

    # Existence un marché
    ext_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    ext_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Conformité du contenu du marché
    conf_cont_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    conf_cont_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Signature du marché par l'attributaire
    sig_mar_att_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    sig_mar_att_date = models.DateField(null=True, blank=True, verbose_name="Date de signature")
    sig_mar_att_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Examen préalable à l'approbation
    exm_pre_app_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    exm_pre_app_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Signature du marché par Autorité Contractante ou approbation
    sig_mar_ac_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    sig_mar_ac_date = models.DateField(null=True, blank=True, verbose_name="Date de signature")
    sig_mar_ac_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Autorité approbatrice
    sig_aco_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    sig_aco_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Numérotation du marché
    num_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    num_mar_date_num = models.DateField(null=True, blank=True, verbose_name="Date de Numérotation")
    num_mar_nom = models.CharField(max_length=255, null=True, blank=True, verbose_name="Numéro")
    num_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Conformité du Numéro du marché
    conf_num_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Conformité du Numéro du marche Constat")
    conf_num_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Montant du marché
    mt_mar = models.PositiveBigIntegerField(null=True, blank=True, verbose_name="Montant")

    # Ecart entre montant estimatif et montant attribué
    ect_mte_mta = models.PositiveBigIntegerField(null=True, blank=True, verbose_name="Montant")

    # Production des pièces fiscales et sociales par attributaire
    prd_pc_fic_soc_att_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    prd_pc_fic_soc_att_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Notification de l'approbation du marché au titulaire
    not_app_mar_ttl = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    not_app_mar_ttl_date_rec = models.DateField(null=True, blank=True, verbose_name="Date de réception par le titulaire")
    not_app_mar_ttl_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Enregistrement du marché
    enr_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    enr_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Transmission de 02 exemplaires du contrat à la DGMP
    trans_dx_exp_ctr_dgmp_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    trans_dx_exp_ctr_dgmp_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Notification de l'ordre de service de démarrage
    not_osd_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    not_osd_date_accr = models.DateField(null=True, blank=True, verbose_name="Date sur l'accusé de réception")
    not_osd_conf = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Conforme")
    not_osd_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    EXHAUSTIVITE = [
        ('Complet', 'Complet'),
        ('Incomplet', 'Incomplet')
    ]

    # Existence et exhaustivité de l'archivage des documents
    ext_exh_arch_doc_exi = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence")
    ext_exh_arch_doc_exh = models.CharField(max_length=9, choices=EXHAUSTIVITE, verbose_name="Exhaustivité")
    ext_exh_arch_doc_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    class Meta:
        verbose_name = "PSO"
        verbose_name_plural = "PSO"
    
    def __str__(self):
        return f"Opération {self.num_aoo} - {self.objet} - {self.ministere} - {self.ac}"
    

class Psl(models.Model):
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
    num_ope = models.CharField(max_length=255, verbose_name="Numéro de l’opération")
    objet = models.CharField(max_length=255, verbose_name="Objet de l’opération")
    nat_oper = models.CharField(max_length=255, choices=NATURE_OPERATION, verbose_name="Nature de l’opération")
    nat_oper_obs = models.TextField(verbose_name="Nature de l’opération Observations", null=True, blank=True)

    # PSPM
    pspm_exist = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence du PSPM")
    
    # Publication du PSPM
    pub_pspm_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Publication du PPM/PSPM")
    pub_pspm_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Inscription de l’opération au PSPM et respect du PSPM
    ope_insc_pspm = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Opération inscrite au PSPM ")
    ope_insc_pspm_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Montant de la dotation / du Crédit 
    mt_dot = models.PositiveBigIntegerField(verbose_name="Montant")
    
    # Situation d'exécution de la ligne budgetaire avant passation
    st_exec_avt_pass_mt = models.PositiveBigIntegerField(verbose_name="Montant disponible")
    
    # Montant de l'estimation
    mt_est = models.PositiveBigIntegerField(verbose_name="Montant")

    # Opération réservée aux PME
    ope_res_pme = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    ope_res_pme_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Examen et validation du DAO par la DGMP 
    exam_val_dao_dgmp_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat", null=True, blank=True)
    exam_val_dao_dgmp_dte_dao_dgmp = models.DateField(verbose_name="Date de réception du DAO à la DGMP", null=True, blank=True)
    exam_val_dao_dgmp_dte_dao_dgmp_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Exigence du quitus de non redevance dans le DAO 
    exg_quitus_dao_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    exg_quitus_dao_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Liste des entreprises consultées (N°CC-Libellé entreprise)
    lst_ent_cslt_lot = models.CharField(max_length=255, verbose_name="lot")
    lst_ent_cslt_nb_ent = models.BigIntegerField(verbose_name="Nombre d'entreprises")
    lst_ent_cslt_ref_acc_pr_cslt_mn_cq_ent = models.CharField(max_length=255, verbose_name=" Référence de l'accord pour consulter moins de cinq entreprises")
    lst_ent_cslt_ent_1 = models.CharField(max_length=255, verbose_name="Entreprise 1")
    lst_ent_cslt_ent_2 = models.CharField(max_length=255, verbose_name="Entreprise 2")
    lst_ent_cslt_ent_3 = models.CharField(max_length=255, verbose_name="Entreprise 3")
    lst_ent_cslt_ent_4 = models.CharField(max_length=255, verbose_name="Entreprise 4")
    lst_ent_cslt_ent_5 = models.CharField(max_length=255, verbose_name="Entreprise 5")

    # Manifestation effective de l'intérêt des entreprises sollicitées à participer à la compétition
    man_eff_int_ent_sol_part_comp_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    man_eff_int_ent_sol_part_comp_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Respect du délai de dépôt de la lettre d'intention
    res_del_dep_let_int_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    res_del_dep_let_int_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Existence d’une liste de retrait du dossier de consultation
    ext_lst_ret_dos_con_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    ext_lst_ret_dos_con_nb_dos_ret = models.PositiveSmallIntegerField(verbose_name="  Nombre de dossiers rétirés")
    ext_lst_ret_dos_con_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Convocation de la COPE
    conv_cojo_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat", null=True, blank=True)
    conv_cojo_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Existence de la COPE
    exist_cojo_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    exist_cojo_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Composition de la COPE
    comp_cojo_conf = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat", null=True, blank=True)
    comp_cojo_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Existence d’une liste de présence des membres de la COPE
    exist_lst_prs_mb_cojo_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    exist_lst_prs_mb_cojo_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
   
    # Existence des mandats des répresentants des membres de la COPE
    exist_mdt_rep_mb_cojo_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    exist_mdt_rep_mb_cojo_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Respect du quorum au niveau de la COPE
    res_qr_nv_cojo_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    res_qr_nv_cojo_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Existence d’une liste de dépôt des plis
    exist_lst_dpt_plis_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    exist_lst_dpt_plis_nb_plis_dep = models.PositiveSmallIntegerField(verbose_name="Nombre de plis déposés", null=True, blank=True)
    exist_lst_dpt_plis_conf_lst_dpt_lst_rtr = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Conformité de la liste de dépôt avec la liste de retrait")
    exist_lst_dpt_plis_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Respect des dates et heures limites de dépôt des plis 
    resp_date_heure_lmt_dep_plis_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    resp_date_heure_lmt_dep_plis_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Respect des dates et heures d'ouverture des plis
    resp_date_heure_lmt_ouv_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    resp_date_heure_lmt_ouv_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Existence d’une liste de présence des soumissionnaires
    ext_lst_prsc_sum_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    ext_lst_prsc_sum_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Existence du procès-verbal d’ouverture des plis
    ext_pv_ouv_plis = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    ext_pv_ouv_plis_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Existence et conformité du rapport d’analyse des offres
    ext_rap_ana = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence du rapport")
    ext_rap_ana_obs = models.TextField(verbose_name="observation", null=True, blank=True)
    
    # Conformité de la COPE au jugement
    conf_cojo_jug_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    conf_cojo_jug_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Existence du procès-verbal de jugement des offres
    ext_pv_jug_off_exst_pv = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence du procès-verbal de jugement")
    ext_pv_jug_off_exst_pv_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
     
    # Respect du délai imparti à la COPE pour ses travaux
    resp_del_imp_cojo_trv_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat",  null=True, blank=True)
    resp_del_imp_cojo_trv_dta_ouv = models.DateField(verbose_name="Date d'ouverture", null=True, blank=True)
    resp_del_imp_cojo_trv_dta_jug = models.DateField(null=True, blank=True, verbose_name="Date de jugement")
    resp_del_imp_cojo_trv_dta_dern_jug = models.DateField(null=True, blank=True, verbose_name="Date du dernier jugement")
    resp_del_imp_cojo_trv_nb_jug = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Nombre de jugements")
    resp_del_imp_cojo_trv_del_trv = models.BigIntegerField(null=True, blank=True, verbose_name="Delai des travaux (en jours ouvrables)")
    resp_del_imp_cojo_trv_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Liste des soumissionnaires & montant de l'offre
    lst_soum_mt_off_lot = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Lot")
    lst_soum_mt_off_nb_soum = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Nombre de soumissionnaires")
    lst_soum_mt_off_soum_1_ncc_nom_ent = models.CharField(max_length=255, verbose_name="NCC & Nom entreprise 1")
    lst_soum_mt_off_soum_1_mt_off = models.PositiveBigIntegerField(verbose_name="Montant de l'offre 1")
    lst_soum_mt_off_soum_2_ncc_nom_ent = models.CharField(max_length=255, verbose_name="NCC & Nom entreprise 2")
    lst_soum_mt_off_soum_2_mt_off = models.PositiveBigIntegerField(verbose_name="Montant de l'offre 2")
    lst_soum_mt_off_soum_3_ncc_nom_ent = models.CharField(max_length=255, verbose_name="NCC & Nom entreprise 3")
    lst_soum_mt_off_soum_3_mt_off = models.PositiveBigIntegerField(verbose_name="Montant de l'offre 3")
    lst_soum_mt_off_soum_4_ncc_nom_ent = models.CharField(max_length=255, verbose_name="NCC & Nom entreprise 4")
    lst_soum_mt_off_soum_4_mt_off = models.PositiveBigIntegerField(verbose_name="Montant de l'offre 4")
    lst_soum_mt_off_soum_5_ncc_nom_ent = models.CharField(max_length=255, verbose_name="NCC & Nom entreprise 5")
    lst_soum_mt_off_soum_5_mt_off = models.PositiveBigIntegerField(verbose_name="Montant de l'offre 5")

    # Notification des résultats aux attributaires
    not_res_att_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    not_res_att_date = models.DateField(null=True, blank=True, verbose_name="Date")
    not_res_att_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Information des soumissionnaires non retenus
    inf_soum_nn_ret_res_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    inf_soum_nn_ret_res_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Attributaire(s)
    att_rs_soc = models.CharField(max_length=255, null=True, blank=True, verbose_name="Raison sociale")
    att_ncc_att = models.CharField(max_length=255, null=True, blank=True, verbose_name="NCC attributaire")
    att_lot = models.CharField(max_length=255, null=True, blank=True, verbose_name="Lot")
    att_mt = models.PositiveBigIntegerField(verbose_name="Montant", null=True, blank=True)
    att_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Respect du délai de recours éventuel
    res_del_rec_evt_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="eConstat")
    res_del_rec_evt_nb_rec =  models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Nombre de recours")
    res_del_rec_evt_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Existence un marché
    ext_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    ext_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Conformité du contenu du marché
    conf_cont_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    conf_cont_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Signature du marché par l'attributaire
    sig_mar_att_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    sig_mar_att_date = models.DateField(null=True, blank=True, verbose_name="Date de signature")
    sig_mar_att_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Examen préalable à l'approbation
    exm_pre_app_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    exm_pre_app_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Signature du marché par Autorité Contractante ou approbation
    sig_mar_ac_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    sig_mar_ac_date = models.DateField(null=True, blank=True, verbose_name="Date de signature")
    sig_mar_ac_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Autorité approbatrice
    sig_aco_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    sig_aco_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Numérotation du marché
    num_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    num_mar_date_num = models.DateField(null=True, blank=True, verbose_name="Date de Numérotation")
    num_mar_num = models.CharField(max_length=255, null=True, blank=True, verbose_name="Numéro")
    num_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Conformité du Numéro du marché
    conf_num_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Conformité du Numéro du marche Constat")
    conf_num_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Montant du marché
    mt_mar = models.PositiveBigIntegerField(null=True, blank=True, verbose_name="Montant")

    # Ecart entre montant estimatif et montant attribué
    ect_mte_mta = models.PositiveBigIntegerField(null=True, blank=True, verbose_name="Montant")

    # Production des pièces fiscales et sociales par l'attributaire
    prd_pc_fic_soc_att_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    prd_pc_fic_soc_att_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Notification de l'approbation du marché au titulaire
    not_app_mar_ttl = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Courrier de notification")
    not_app_mar_ttl_date_rec = models.DateField(null=True, blank=True, verbose_name="Date de notification")
    not_app_mar_ttl_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Enregistrement du marché
    enr_mar_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    enr_mar_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Transmission de 02 exemplaires du contrat à la DGMP
    trans_dx_exp_ctr_dgmp_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    trans_dx_exp_ctr_dgmp_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Notification de l'ordre de service de démarrage
    not_osd_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    not_osd_date_accr = models.DateField(null=True, blank=True, verbose_name="Date sur l'accusé de réception")
    not_osd_conf = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Conforme")
    not_osd_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    EXHAUSTIVITE = [
        ('Complet', 'Complet'),
        ('Incomplet', 'Incomplet')
    ]

    # Existence et exhaustivité de l'archivage des documents
    ext_exh_arch_doc_exi = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence")
    ext_exh_arch_doc_exh = models.CharField(max_length=9, choices=EXHAUSTIVITE, verbose_name="Exhaustivité")
    ext_exh_arch_doc_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    class Meta:
        verbose_name = "PSL"
        verbose_name_plural = "PSL"
    
    def __str__(self):
        return f"Opération {self.num_ope} - {self.objet} - {self.ministere} - {self.ac}"
    

class Psc(models.Model):
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
    num_ope = models.CharField(max_length=255, verbose_name="Numéro de l’opération (N° formulaire de demande de cotation)")
    objet = models.CharField(max_length=255, verbose_name="Objet de l’opération")
    nat_oper = models.CharField(max_length=255, choices=NATURE_OPERATION, verbose_name="Nature de l’opération")
    nat_oper_obs = models.TextField(verbose_name="Nature de l’opération Observations", null=True, blank=True)

    # PSPM
    pspm_exist = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence du PSPM")
    
    # Publication du PSPM
    pub_pspm_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Publication du PPM/PSPM")
    pub_pspm_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Inscription de l’opération au PSPM et respect du PSPM
    ope_insc_pspm = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Opération inscrite au PSPM ")
    ope_insc_pspm_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Montant de la dotation / du Crédit 
    mt_dot = models.PositiveBigIntegerField(verbose_name="Montant")
    
    # Situation d'exécution de la ligne budgetaire avant passation
    st_exec_avt_pass_mt = models.PositiveBigIntegerField(verbose_name="Montant disponible")
    
    # Montant de l'estimation
    mt_est = models.PositiveBigIntegerField(verbose_name="Montant")

    # Opération réservée aux PME
    ope_res_pme = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    ope_res_pme_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Formulaire de demande de cotation
    form_dem_cot_conf_mod_elb_dgmp = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Conforme au modèle élaboré par la DGMP ", null=True, blank=True)
    form_dem_cot_dte_trans_form = models.DateField(verbose_name="Date de transmission du formulaire", null=True, blank=True)
    form_dem_cot_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Liste des entreprises consultées & montant des offres (N°CC-Libellé entreprise))
    lst_ent_cslt_nb_ent = models.PositiveSmallIntegerField(verbose_name="Nombre de soumissionnaires", null=True, blank=True)
    lst_ent_cslt_ref_acc_pr_cslt_mn_cq_ent = models.CharField(max_length=255, verbose_name="Référence de l'accord pour consulter moins de cinq entreprises", null=True, blank=True)
    lst_ent_cslt_ent_1_ncc_nom = models.CharField(max_length=255, verbose_name="NCC et nom de l'entreprise 1", null=True, blank=True)    
    lst_ent_cslt_ent_1_mtt = models.CharField(max_length=255, verbose_name="Montant de l'offre de l'entreprise 1", null=True, blank=True)
    lst_ent_cslt_ent_2_ncc_nom = models.CharField(max_length=255, verbose_name="NCC et nom de l'entreprise 2", null=True, blank=True)    
    lst_ent_cslt_ent_2_mtt = models.CharField(max_length=255, verbose_name="Montant de l'offre de l'entreprise 2", null=True, blank=True)
    lst_ent_cslt_ent_3_ncc_nom = models.CharField(max_length=255, verbose_name="NCC et nom de l'entreprise 3", null=True, blank=True)    
    lst_ent_cslt_ent_3_mtt = models.CharField(max_length=255, verbose_name="Montant de l'offre de l'entreprise 3", null=True, blank=True)

    # formulaire de sélection
    form_sel_ext = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence", null=True, blank=True)
    form_sel_conf_mod_dgmp = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Conforme au modèle DGMP", null=True, blank=True)
    form_sel_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Date et signature du formulaire de selection
    dte_sig_form_sel_sig = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Signature", null=True, blank=True)
    dte_sig_form_sel_dte = models.DateField(verbose_name="Date", null=True, blank=True)
    dte_sig_form_sel_qlte_sig = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Qualité du signataire", null=True, blank=True)
    dte_sig_form_sel_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Attributaire(s)
    att_lot = models.CharField(max_length=255, null=True, blank=True, verbose_name="Lot")
    att_rs_soc = models.CharField(max_length=255, null=True, blank=True, verbose_name="Raison sociale")
    att_ncc_att = models.CharField(max_length=255, null=True, blank=True, verbose_name="NCC attributaire")
    att_mt = models.PositiveBigIntegerField(verbose_name="Montant", null=True, blank=True)
    att_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Ecart entre montant estimatif et montant attribué
    ect_mte_mta = models.PositiveBigIntegerField(null=True, blank=True, verbose_name="Montant")

    # Notification de l'attribution au (x) soumissionnaire (s) retenu (s)
    not_att_soum_ret_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    not_att_soum_ret_date = models.DateField(null=True, blank=True, verbose_name="Date")
    not_att_soum_ret_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Information des soumissionnaires non retenus
    inf_soum_nn_ret_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    inf_soum_nn_ret_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Notification de l'ordre de service de démarrage
    not_osd_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    not_osd_date_accr = models.DateField(null=True, blank=True, verbose_name="Date sur l'accusé de réception")
    not_osd_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    EXHAUSTIVITE = [
        ('Complet', 'Complet'),
        ('Incomplet', 'Incomplet')
    ]

    # Existence et exhaustivité de l'archivage des documents
    ext_exh_arch_doc_exi = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence")
    ext_exh_arch_doc_exh = models.CharField(max_length=9, choices=EXHAUSTIVITE, verbose_name="Exhaustivité")
    ext_exh_arch_doc_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    class Meta:
        verbose_name = "PSC"
        verbose_name_plural = "PSC"
    
    def __str__(self):
        return f"Opération {self.num_ope} - {self.objet} - {self.ministere} - {self.ac}"
    

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
    objet = models.CharField(max_length=255, verbose_name="Objet de l’opération")
    nat_oper = models.CharField(max_length=255, choices=NATURE_OPERATION, verbose_name="Nature de l’opération")
    nat_oper_obs = models.TextField(verbose_name="Nature de l’opération Observations", null=True, blank=True)

    # Montant de la dotation / ou du Crédit 
    mt_dot = models.PositiveBigIntegerField(verbose_name="Montant")
    
    # Situation d'exécution de la ligne budgetaire avant passation
    st_exec_avt_pass_mt = models.PositiveBigIntegerField(verbose_name="Montant disponible")
    
    # PSPM
    pspm_exist = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Existence du PSPM")
    
    # Publication du PSPM
    pub_pspm_cst = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Publication du PPM/PSPM")
    pub_pspm_obs = models.TextField(verbose_name="Observations", null=True, blank=True)
    
    # Inscription de l’opération au PSPM et respect du PSPM
    ope_insc_pspm = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Opération inscrite au PSPM ")
    ope_insc_pspm_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Montant de l'estimation
    mt_est = models.PositiveBigIntegerField(verbose_name="Montant")

    # Opération réservée aux PME
    ope_res_pme = models.CharField(max_length=3, choices=OUI_NON, verbose_name="Constat")
    ope_res_pme_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Date de commande
    dte_commande = models.DateField(verbose_name="Date")
    dte_commande_obs = models.TextField(verbose_name="Observations", null=True, blank=True)

    # Attributaire(s)
    att_rs_soc = models.CharField(max_length=255, null=True, blank=True, verbose_name="Raison sociale")
    att_ncc_att = models.CharField(max_length=255, null=True, blank=True, verbose_name="NCC attributaire")
    att_mt = models.PositiveBigIntegerField(verbose_name="Montant", null=True, blank=True)
    att_obs = models.TextField(null=True, blank=True, verbose_name="Observations")

    # Ecart entre montant estimatif et montant attribué
    ect_mte_mta = models.PositiveBigIntegerField(null=True, blank=True, verbose_name="Montant")

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
        return f"Opération- {self.objet} - {self.ministere} - {self.ac}"