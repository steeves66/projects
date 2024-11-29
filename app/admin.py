from django.contrib import admin
from django.contrib.auth.models import User, Group
from admin_extra_buttons.api import ExtraButtonsMixin, button
from django.http import HttpResponse
from .models import Aoo, Aor, Gag, Pso, Psl, Psc, Psd
from django.conf import settings
from django.http import HttpResponse
# from .functions import data_to_excel_file
from .functions import ExcelFile


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.site_header = "DGMP"
admin.site.site_title = "DGMP Contrôle à posteriori"
admin.site.index_title = "Contrôle à posteriori Procédures"


actions = ["test"]
def test(self, request, queryset):
    pass


@admin.register(Aoo)
class AooAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    # def __init__(self, model, admin_site):
    #     self.list_display = [field.name for field in model._meta.fields]
    #    super().__init__(model, admin_site)
    actions = ["test"]
    def test(self, request, queryset):
        pass


    list_display = ['ministere']

    fieldsets = (
        ("Généralites", {
            'classes': ('collapse',),
            'fields': ('agent_cont', 'date_contr', 'ministere', 'ac', 'pers_res', 'imputation', 'num_aoo', 'objet', 'nat_oper', 'nat_oper_obs',)
        }),
        ("PPM", {
            'classes': ('collapse',),
            'fields': ('ppm_exist', 'ppm_obs',)
        }),
        ("Publication du PPM", {
            'classes': ('collapse',),
            'fields': ('pub_ppm_cst', 'pub_ppm_obs', )
        }),
        ("Inscription de l’opération au PPM", {
            'classes': ('collapse',),
            'fields': ('ope_insc_ppm', 'ope_insc_ppm_obs',)
        }),
        (None, {
            'classes': ('collapse',),
            'fields': ('mt_dot', 'st_exec_avt_pass_mt', 'mt_est',)
        }),
        ('Opération réservée aux PME', {
            'classes': ('collapse',),
            'fields': ('ope_res_pme', 'ope_res_pme_obs',)
        }),
        ('Examen et validation du DAO par la DGMP', {
            'classes': ('collapse',),
            'fields': ('exam_val_dao_dgmp_cst', 'exam_val_dao_dgmp_dte_dao_dgmp', 'exam_val_dao_dgmp_dte_dao_dgmp_obs')
        }),
        ('Exigence du quitus de non redevance dans le DAO ', {
            'classes': ('collapse',),
            'fields': ('exg_quitus_dao_cst', 'exg_quitus_dao_obs',)
        }),
        ("Garantie de l'offre comprise entre 1 et 1,5%", {
            'classes': ('collapse',),
            'fields': ('gar_offre_cst', 'gar_offre_cst_obs', )
        }),
        ("Publication de l'avis d'appel d'offres dans le BOMP", {
            'classes': ('collapse',),
            'fields': ('pub_aao_bomp_cst', 'pub_aao_bomp_date', 'pub_aao_bomp_no_bomp', 'pub_aao_bomp_duree', 'pub_aao_bomp_obs')
        }),
        ("Existence d’une liste de retrait du DAO", {
            'classes': ('collapse',),
            'fields': ('exist_lst_rtr_dao_cst', 'exist_lst_rtr_dao_nb_dos_ret', 'exist_lst_rtr_dao_obs',)
        }),
        ("Convocation de la COJO", {
            'classes': ('collapse',),
            'fields': ('conv_cojo_cst', 'conv_cojo_obs',)
        }),
        ("Existence de la COJO", {
            'classes': ('collapse',),
            'fields': ('exist_cojo_cst', 'exist_cojo_obs',)
        }),
        ("Composition de la COJO", {
            'classes': ('collapse',),
            'fields': ('comp_cojo_conf', 'comp_cojo_obs',)
        }),
        ("Existence d’une liste de présence des membres de la COJO", {
            'classes': ('collapse',),
            'fields': ('exist_lst_prs_mb_cojo_cst', 'exist_lst_prs_mb_cojo_obs',)
        }),
        ("Existence des mandats  des répresentants des membres de la COJO", {
            'classes': ('collapse',),
            'fields': ('exist_mdt_rep_mb_cojo_cst', 'exist_mdt_rep_mb_cojo_obs',)
        }),
        ("Respect du quorum au niveau de la COJO", {
            'classes': ('collapse',),
            'fields': ('res_qr_nv_cojo_cst', 'res_qr_nv_cojo_obs',)
        }),
        ("Existence d’une liste de dépôt des plis", {
            'classes': ('collapse',),
            'fields': ('exist_lst_dpt_plis_cst', 'exist_lst_dpt_plis_nb_plis_dep', 'exist_lst_dpt_plis_conf_lst_dpt_lst_rtr', 'exist_lst_dpt_plis_obs')
        }),
        ("Respect des date et heure limites de dépôt des plis", {
            'classes': ('collapse',),
            'fields': ('resp_date_heure_lmt_dep_plis_cst', 'resp_date_heure_lmt_dep_plis_obs',)
        }),
        ("Respect des date et heure d'ouverture des plis", {
            'classes': ('collapse',),
            'fields': ('resp_date_heure_lmt_ouv_cst', 'resp_date_heure_lmt_ouv_obs',)
        }),
        ("Existence d’une liste de présence des soumissionnaires", {
            'classes': ('collapse',),
            'fields': ('ext_lst_prsc_sum_cst', 'ext_lst_prsc_sum_obs',)
        }),
        ("Existence du procès-verbal d’ouverture des plis", {
            'classes': ('collapse',),
            'fields': ('ext_pv_ouv_plis', 'ext_pv_ouv_plis_obs',)
        }),
        ("Existence du rapport d’analyse des offres", {
            'classes': ('collapse',),
            'fields': ('ext_rap_ana', 'ext_rap_ana_obs',)
        }),
        ("Conformité de la COJO au jugement", {
            'classes': ('collapse',),
            'fields': ('conf_cojo_jug_cst', 'conf_cojo_jug_obs',)
        }),
        ("Existence du procès-verbal de jugement des offres", {
            'classes': ('collapse',),
            'fields': ('ext_pv_jug_off_exst_pv', 'ext_pv_jug_off_exst_pv_obs',)
        }),
        ("Respect du délai imparti à la COJO pour ses travaux", {
            'classes': ('collapse',),
            'fields': ('resp_del_imp_cojo_trv_cst', 'resp_del_imp_cojo_trv_dta_ouv', 'resp_del_imp_cojo_trv_dta_jug', 'resp_del_imp_cojo_trv_dta_dern_jug', 'resp_del_imp_cojo_trv_nb_jug', 'resp_del_imp_cojo_trv_del_trv', 'resp_del_imp_cojo_trv_obs')
        }),
        ("Publication des résultats de la COJO par la DGMP", {
            'classes': ('collapse',),
            'fields': ('pub_res_cojo_dgmp_cst', 'pub_res_cojo_dgmp_date_pub', 'pub_res_cojo_dgmp_no_bomp', 'pub_res_cojo_dgmp_obs',)
        }),
        ("Notification des résultats aux attributaires", {
            'classes': ('collapse',),
            'fields': ('not_res_att_cst', 'not_res_att_date', 'not_res_att_obs',)
        }),
        ("Information des soumissionnaires non retenus sur les résultats", {
            'classes': ('collapse',),
            'fields': ('inf_soum_nn_ret_res_cst', 'inf_soum_nn_ret_res_obs',)
        }),
        ("Attributaire(s)", {
            'classes': ('collapse',),
            'fields': ('att_rs_soc', 'att_ncc_att', 'att_lot', 'att_mt', 'att_obs')
        }),
        ("Respect du délai de recours éventuel", {
            'classes': ('collapse',),
            'fields': ('res_del_rec_evt_cst', 'res_del_rec_evt_obs', )
        }),
        ("Restitution des actes de garantie aux soumissionnaires non retenus", {
            'classes': ('collapse',),
            'fields': ('rst_act_gar_soum_nn_ret_cst', 'rst_act_gar_soum_nn_ret_rspt_del_rst', 'rst_act_gar_soum_nn_ret_rspt_del_obs')
        }),
        ("Existence un marché", {
            'classes': ('collapse',),
            'fields': ('ext_mar_cst', 'ext_mar_obs', )
        }),
        ("Conformité du contenu du marché", {
            'classes': ('collapse',),
            'fields': ('conf_cont_mar_cst', 'conf_cont_mar_obs', )
        }),
        ("Signature du marché par attributaire", {
            'classes': ('collapse',),
            'fields': ('sig_mar_att_cst', 'sig_mar_att_date', 'sig_mar_att_obs')
        }),
        ("Signature du marché par Autorité Contractante", {
            'classes': ('collapse',),
            'fields': ('sig_mar_ac_cst', 'sig_mar_ac_date', 'sig_mar_ac_obs')
        }),
        ("Signature de l'Autorité compétente", {
            'classes': ('collapse',),
            'fields': ('sig_aco_cst', 'sig_aco_obs', )
        }),
        ("Numérotation du marché", {
            'classes': ('collapse',),
            'fields': ('num_mar_cst', 'num_mar_date_num', 'num_mar_nom', 'num_mar_obs')
        }),
        ("Conformité du Numéro du marché", {
            'classes': ('collapse',),
            'fields': ('conf_num_mar_cst', 'conf_num_mar_obs', )
        }),
        ("Montant du marché", {
            'classes': ('collapse',),
            'fields': ('mt_mar', 'ect_mte_mta',)
        }),
        ("Production des pièces fiscales et sociales par attributaire", {
            'classes': ('collapse',),
            'fields': ('prd_pc_fic_soc_att_cst', 'prd_pc_fic_soc_att_obs',)
        }),
        ("Examen préalable à l'approbation", {
            'classes': ('collapse',),
            'fields': ('exm_pre_app_cst', 'exm_pre_app_dte_trm_prjm_dgmp', 'exm_pre_app_dte_trm_rslt_exm_dgmp_ac', 'exm_pre_app_obs')
        }),
        ("Approbation du marché", {
            'classes': ('collapse',),
            'fields': ('app_mar_cst', 'app_mar_date', 'app_mar_obs', )
        }),
        ("Autorité approbatrice ou organe approbateur compétent", {
            'classes': ('collapse',),
            'fields': ('aut_app_cst', 'aut_app_obs', )
        }),
        ("Notification de l'approbation du marché au titulaire", {
            'classes': ('collapse',),
            'fields': ('not_app_mar_ttl', 'not_app_mar_ttl_date_rec', 'not_app_mar_ttl_obs')
        }),
        ("Enregistrement du marché", {
            'classes': ('collapse',),
            'fields': ('enr_mar_cst', 'enr_mar_obs',)
        }),
        ("Transmission de 02 exemplaires du contrat à la DGMP", {
            'classes': ('collapse',),
            'fields': ('trans_dx_exp_ctr_dgmp_cst', 'trans_dx_exp_ctr_dgmp_obs',)
        }),
        ("Notification de l'ordre de service de démarrage", {
            'classes': ('collapse',),
            'fields': ('not_osd_cst', 'not_osd_date_accr', 'not_osd_conf', 'not_osd_obs')
        }),
        ("Existence et exhaustivité de l'archivage des documents", {
            'classes': ('collapse',),
            'fields': ('ext_exh_arch_doc_exi', 'ext_exh_arch_doc_exh', 'ext_exh_arch_doc_obs',)
        }),
        ("Temps total pour la conduite de l’opération", {
            'classes': ('collapse',),
            #'fields': ('tps_tt_cdt_ope_nb_jrs', 'tps_tt_cdt_ope_nb_obs',)
            'fields': ('tps_tt_cdt_ope_nb_obs',)
        }),
    )

    # Bouton pour exporter en Excel
    @button(label="Exporter en Excel", html_attrs={'style': 'background-color:#00AA00;color:black'})
    def export_to_excel(self, request):
        file = ExcelFile("AOO-Guide contrôle a posteriori procédures cLassiques.xlsx", 
                         "GUIDE_PC_AOO_VF", 
                         7, 
                         1, 
                         'Aoo', 
                         "DATA_AOO",
                         4, 
                         1)
        workbook = file.create_excel_file()
        # Créer une réponse HTTP pour envoyer le fichier Excel
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Appel_offre_ouvert.xlsx'

        # Sauvegarder le fichier Excel dans la réponse
        workbook.save(response)
        return response
    

@admin.register(Aor)
class AorAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super().__init__(model, admin_site)

    fieldsets = (
        ("Généralites", {
            'classes': ('collapse',),
            'fields': ('agent_cont', 'date_contr', 'ministere', 'ac', 'pers_res', 'imputation', 'num_aoo', 'objet', 'nat_oper', 'nat_oper_obs',)
        }),
        ("PPM", {
            'classes': ('collapse',),
            'fields': ('ppm_exist',)
        }),
        ("Publication du PPM", {
            'classes': ('collapse',),
            'fields': ('pub_ppm_cst', 'pub_ppm_obs', )
        }),
        ("Inscription de l’opération au PPM", {
            'classes': ('collapse',),
            'fields': ('ope_insc_ppm', 'ope_insc_ppm_obs',)
        }),
        ("Montant de la dotation / du Crédit", {
            'classes': ('collapse',),
            'fields': ('mt_dot',)
        }),
        ("Situation d'exécution de la ligne budgetaire avant passation", {
            'classes': ('collapse',),
            'fields': ('st_exec_avt_pass_mt_disp',)
        }),
        ("Montant de l'estimation", {
            'classes': ('collapse',),
            'fields': ('mt_est',)
        }),
        ('Opération réservée aux PME', {
            'classes': ('collapse',),
            'fields': ('ope_res_pme', 'ope_res_pme_obs',)
        }),
        ('Mode de sélection des entreprises', {
            'classes': ('collapse',),
            'fields': ('mod_sel_ent',)
        }),
        ("Publication de l'avis de préqualification ou de l'AMI dans le BOMP et sur le site de la DGMP", {
            'classes': ('collapse',),
            'fields': ('pub_adp_ami_bomp_int_cst', 'pub_adp_ami_bomp_int_date', 'pub_adp_ami_bomp_int_obs')
        }),
        ("Lettre d'invitation de l'AC aux entreprises", {
            'classes': ('collapse',),
            'fields': ('lt_inv_ac_ent_cst', 'lt_inv_ac_ent_nb', )
        }),
        ("Accord de participation des candidats sollicités", {
            'classes': ('collapse',),
            'fields': ('acd_part_cand_sol_cst', 'acd_part_cand_sol_obs', )
        }),
        ("Autorisation de recourir à l'AOR", {
            'classes': ('collapse',),
            'fields': ('aut_rec_aor_cst', 'aut_rec_aor_ref', )
        }),
        ("Liste des entreprises autorisées à participer à la concurrence", {
            'classes': ('collapse',),
            'fields': ('ent_1', 'ent_2', 'ent_3', 'ent_4', 'ent_5' )
        }),
        ("Examen DAO / DP à la DGMP", {
            'classes': ('collapse',),
            'fields': ('exm_val_dao_dp_dgmp_cst', 'exm_val_dao_dp_dgmp_date', 'exm_val_dao_dp_dgmp_obs',)
        }),

        ("Exigence du quitus de non redevance dans le DAO", {
            'classes': ('collapse',),
            'fields': ('exg_quitus_dao_cst', 'exg_quitus_dao_obs',)
        }),

        ("Garantie de l'offre comprise entre 1 et 1,5%", {
            'classes': ('collapse',),
            'fields': ('gar_offre_cst', 'gar_offre_cst_obs', )
        }),

        ("Transmission des lettres d'invitation aux candidats autorisés à participer à la concurrence", {
            'classes': ('collapse',),
            'fields': ('trm_let_inv_cnd_aut_prt_ccr_cst', 'trm_let_inv_cnd_aut_prt_ccr_date', 'trm_let_inv_cnd_aut_prt_ccr_obs')
        }),

        ("Convocation COJO", {
            'classes': ('collapse',),
            'fields': ('conv_cojo_cst', 'conv_cojo_obs', )
        }),

        ("Existence de la COJO", {
            'classes': ('collapse',),
            'fields': ('exist_cojo_cst', 'exist_cojo_obs',)
        }),

        ("Composition de la COJO", {
            'classes': ('collapse',),
            'fields': ('comp_cojo_conf', 'comp_cojo_obs',)
        }),

        ("Existence d’une liste de présence des membres de la COJO", {
            'classes': ('collapse',),
            'fields': ('exist_lst_prs_mb_cojo_cst', 'exist_lst_prs_mb_cojo_obs',)
        }),

        ("Existence des mandats  des répresentants des membres de la COJO", {
            'classes': ('collapse',),
            'fields': ('exist_mdt_rep_mb_cojo_cst', 'exist_mdt_rep_mb_cojo_obs',)
        }),

        ("Respect du quorum au niveau de la COJO", {
            'classes': ('collapse',),
            'fields': ('res_qr_nv_cojo_cst', 'res_qr_nv_cojo_obs',)
        }),

        ("Existence d’une liste de dépôt des plis", {
            'classes': ('collapse',),
            'fields': ('exist_lst_dpt_plis_cst', 'exist_lst_dpt_plis_nb_plis_dep', 'exist_lst_dpt_plis_conf_lst_dpt_lst_rtr', 'exist_lst_dpt_plis_obs')
        }),

        ("Respect des dates et heures limites de dépôt des plis", {
            'classes': ('collapse',),
            'fields': ('resp_date_heure_lmt_dep_plis_cst', 'resp_date_heure_lmt_dep_plis_obs',)
        }),

        ("Respect des dates et heures d'ouverture des plis", {
            'classes': ('collapse',),
            'fields': ('resp_date_heure_lmt_ouv_cst', 'resp_date_heure_lmt_ouv_obs',)
        }),

        ("Nombre de plis reçus à l'ouverture", {
            'classes': ('collapse',),
            'fields': ('nb_plis_rec_ouv_dep', 'nb_plis_rec_ouv_obs',)
        }),

        ("Existence d’une liste de présence des soumissionnaires", {
            'classes': ('collapse',),
            'fields': ('ext_lst_prsc_sum_cst', 'ext_lst_prsc_sum_obs',)
        }),

        ("Existence du procès-verbal d’ouverture des plis", {
            'classes': ('collapse',),
            'fields': ('ext_pv_ouv_plis', 'ext_pv_ouv_plis_obs',)
        }),
        
        ("Existence du rapport d’analyse des offres", {
            'classes': ('collapse',),
            'fields': ('ext_rap_ana', 'ext_rap_ana_obs',)
        }),

        ("Conformité de la COJO au jugement", {
            'classes': ('collapse',),
            'fields': ('conf_cojo_jug_cst', 'conf_cojo_jug_obs',)
        }),

        ("Existence du procès-verbal de jugement des offres", {
            'classes': ('collapse',),
            'fields': ('ext_pv_jug_off_exst_pv', 'ext_pv_jug_off_exst_pv_obs',)
        }),

        ("Respect du délai imparti à la COJO pour ses travaux", {
            'classes': ('collapse',),
            'fields': ('resp_del_imp_cojo_trv_cst', 'resp_del_imp_cojo_trv_dta_ouv', 'resp_del_imp_cojo_trv_dta_jug', 'resp_del_imp_cojo_trv_dta_dern_jug', 'resp_del_imp_cojo_trv_nb_jug', 'resp_del_imp_cojo_trv_del_trv', 'resp_del_imp_cojo_trv_obs')
        }),

        ("Publication des résultats de la COJO par la DGMP", {
            'classes': ('collapse',),
            'fields': ('pub_res_cojo_dgmp_cst', 'pub_res_cojo_dgmp_date_pub', 'pub_res_cojo_dgmp_no_bomp', 'pub_res_cojo_dgmp_obs',)
        }),

        ("Notification des résultats aux attributaires", {
            'classes': ('collapse',),
            'fields': ('not_res_att_cst', 'not_res_att_date', 'not_res_att_obs',)
        }),

        ("Information des soumissionnaires sur les résultats", {
            'classes': ('collapse',),
            'fields': ('inf_soum_res_cst', 'inf_soum_res_obs',)
        }),

        ("Attributaire(s)", {
            'classes': ('collapse',),
            'fields': ('att_rs_soc', 'att_ncc_att', 'att_lot', 'att_mt', 'att_obs')
        }),

        ("Respect du délai de recours éventuel", {
            'classes': ('collapse',),
            'fields': ('res_del_rec_evt_cst', 'res_del_rec_evt_obs', )
        }),

        ("Restitution des actes de garantie aux soumissionnaires non retenus", {
            'classes': ('collapse',),
            'fields': ('rst_act_gar_soum_nn_ret_cst', 'rst_act_gar_soum_nn_ret_rspt_del_rst', 'rst_act_gar_soum_nn_ret_rspt_del_obs')
        }),

        ("Existence un marché", {
            'classes': ('collapse',),
            'fields': ('ext_mar_cst', 'ext_mar_obs', )
        }),

        ("Conformité du contenu du marché", {
            'classes': ('collapse',),
            'fields': ('conf_cont_mar_cst', 'conf_cont_mar_obs', )
        }),

        ("Signature du marché par attributaire", {
            'classes': ('collapse',),
            'fields': ('sig_mar_att_cst', 'sig_mar_att_date', 'sig_mar_att_obs')
        }),

        ("Signature du marché par Autorité Contractante", {
            'classes': ('collapse',),
            'fields': ('sig_mar_ac_cst', 'sig_mar_ac_date', 'sig_mar_ac_obs')
        }),

        ("Signature de l'Autorité compétente", {
            'classes': ('collapse',),
            'fields': ('sig_aco_cst', 'sig_aco_obs', )
        }),

        ("Numérotation du marché", {
            'classes': ('collapse',),
            'fields': ('num_mar_cst', 'num_mar_date_num', 'num_mar_nom', 'num_mar_obs')
        }),

        ("Conformité du Numéro du marché", {
            'classes': ('collapse',),
            'fields': ('conf_num_mar_cst', 'conf_num_mar_obs', )
        }),

        ("Montant du marché", {
            'classes': ('collapse',),
            'fields': ('mt_mar',)
        }),

        ("Ecart entre montant estimatif et montant attribué", {
            'classes': ('collapse',),
            'fields': ('ect_mte_mta',)
        }),

        ("Production des pièces fiscales et sociales par attributaire", {
            'classes': ('collapse',),
            'fields': ('prd_pc_fic_soc_att_cst', 'prd_pc_fic_soc_att_obs',)
        }),

        ("Examen préalable à l'approbation", {
            'classes': ('collapse',),
            'fields': ('exm_pre_app_cst', 'exm_pre_app_dte_trm_prjm_dgmp', 'exm_pre_app_dte_trm_rslt_exm_dgmp_ac', 'exm_pre_app_obs')
        }),

        ("Approbation du marché", {
            'classes': ('collapse',),
            'fields': ('app_mar_cst', 'app_mar_date', 'app_mar_obs', )
        }),

        ("Autorité approbatrice ou organe approbateur compétent", {
            'classes': ('collapse',),
            'fields': ('aut_app_cst', 'aut_app_obs', )
        }),

        ("Notification de l'approbation du marché au titulaire", {
            'classes': ('collapse',),
            'fields': ('not_app_mar_ttl', 'not_app_mar_ttl_date_rec', 'not_app_mar_ttl_obs')
        }),

        ("Enregistrement du marché", {
            'classes': ('collapse',),
            'fields': ('enr_mar_cst', 'enr_mar_obs',)
        }),

        ("Transmission de 02 exemplaires du contrat à la DGMP", {
            'classes': ('collapse',),
            'fields': ('trans_dx_exp_ctr_dgmp_cst', 'trans_dx_exp_ctr_dgmp_obs',)
        }),

        ("Notification de l'ordre de service de démarrage", {
            'classes': ('collapse',),
            'fields': ('not_osd_cst', 'not_osd_date_accr', 'not_osd_conf', 'not_osd_obs')
        }),

        ("Existence et exhaustivité de l'archivage des documents", {
            'classes': ('collapse',),
            'fields': ('ext_exh_arch_doc_exi', 'ext_exh_arch_doc_exh', 'ext_exh_arch_doc_obs',)
        }),

        # ("Temps total pour la conduite de l’opération", {
        #    'classes': ('collapse',),
        #    'fields': ('tps_tt_cdt_ope_nb_jrs', 'tps_tt_cdt_ope_nb_obs',)
        # }),
    ) 

    @button(label="Exporter en Excel", html_attrs={'style': 'background-color:#00AA00;color:black'})
    def export_to_excel(self, request):
        file = ExcelFile("AOR-Guide contrôle a posteriori Procédures CLassiques.xlsx", 
                         "GUIDE_AOR_2", 
                         7, 
                         1, 
                         'Aor',
                         "DATA_AOR_2",  
                         4, 
                         1)
        workbook = file.create_excel_file()
        # Créer une réponse HTTP pour envoyer le fichier Excel
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Appel_offre_restreint.xlsx'

        # Sauvegarder le fichier Excel dans la réponse
        workbook.save(response)
        return response 


@admin.register(Gag)
class GagAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super().__init__(model, admin_site)

    fieldsets = (
        ("Généralites", {
            'classes': ('collapse',),
            'fields': ("agent_cont", "date_contr", "ministere", "ac", "pers_res", "imputation", "objet", "nat_oper",)
        }),
        ("Préparation du PPM", {
            'classes': ('collapse',),
            'fields': ("ppm_exist",)
        }),
        ("Publication du PPM", {
            'classes': ('collapse',),
            'fields': ("pub_ppm_cst", "pub_ppm_obs",)
        }),
        ("Inscription de l’opération au PPM et respect du PPM", {
            'classes': ('collapse',),
            'fields': ("ope_insc_ppm", "ope_insc_ppm_obs",)
        }),
        ("Montant de la dotation / du Crédit", {
            'classes': ('collapse',),
            'fields': ("mt_dot",)
        }),
        ("Montant de l'Estimation", {
            'classes': ('collapse',),
            'fields': ("mt_est",)
        }),
        ("Situation d'exécution de la ligne budgetaire avant passation", {
            'classes': ('collapse',),
            'fields': ("st_exec_avt_pass_mt",)
        }),
        ("Opération réservée aux PME", {
            'classes': ('collapse',),
            'fields': ("ope_res_pme", "ope_res_pme_obs",)
        }),
        ("PV de négociation ou de consultation", {
            'classes': ('collapse',),
            'fields': ("pv_neg_consult_cst", "pv_neg_consult_obs",)
        }),
        ("Autorisation de recourir au Gré à Gré", {
            'classes': ('collapse',),
            'fields': ("aut_rec_gag_cst", "aut_rec_gag_ref",)
        }),
        ("Attributaire(s)", {
            'classes': ('collapse',),
            'fields': ("att_rs_soc", "att_ncc_att", "att_lot", "att_mt", "att_obs",)
        }),
        ("Existence un marché", {
            'classes': ('collapse',),
            'fields': ("ext_mar_cst", "ext_mar_obs",)
        }),
        ("Conformité du contenu du marché", {
            'classes': ('collapse',),
            'fields': ("conf_cont_mar_cst", "conf_cont_mar_obs",)
        }),
        ("Signature du marché par attributaire", {
            'classes': ('collapse',),
            'fields': ("sig_mar_att_cst", "sig_mar_att_date", "sig_mar_att_obs",)
        }),
        ("Signature du marché par Autorité Contractante", {
            'classes': ('collapse',),
            'fields': ("sig_mar_ac_cst", "sig_mar_ac_date", "sig_mar_ac_obs",)
        }),
        ("Signature de l'Autorité compétente", {
            'classes': ('collapse',),
            'fields': ("sig_aco_cst", "sig_aco_obs",)
        }),
        ("Numérotation du marché", {
            'classes': ('collapse',),
            'fields': ("num_mar_cst", "num_mar_date_num", "num_mar_nom",)
        }),
        ("Conformité du Numéro du marché", {
            'classes': ('collapse',),
            'fields': ("conf_num_mar_cst", "conf_num_mar_obs",)
        }),
        ("Montant du marché", {
            'classes': ('collapse',),
            'fields': ("mt_mar",)
        }),
        ("Production des pièces fiscales et sociales par attributaire", {
            'classes': ('collapse',),
            'fields': ("prd_pc_fic_soc_att_cst", "prd_pc_fic_soc_att_obs",)
        }),
        ("Examen préalable à l'approbation", {
            'classes': ('collapse',),
            'fields': ("exm_pre_app_cst", "exm_pre_app_dte_trm_prjm_dgmp", "exm_pre_app_dte_trm_rslt_exm_dgmp_ac", "exm_pre_app_obs",)
        }),
        ("Approbation du marché", {
            'classes': ('collapse',),
            'fields': ("app_mar_cst", "app_mar_date", "app_mar_obs",)
        }),
        ("Autorité approbatrice ou organe approbateur compétent", {
            'classes': ('collapse',),
            'fields': ("aut_app_cst", "aut_app_obs",)
        }),
        ("Notification de l'approbation du marché au titulaire", {
            'classes': ('collapse',),
            'fields': ("not_app_mar_ttl", "not_app_mar_ttl_date_rec", "not_app_mar_ttl_obs",)
        }),
        ("Enregistrement du marché", {
            'classes': ('collapse',),
            'fields': ("enr_mar_cst", "enr_mar_obs")
        }),
        ("Notification de l'ordre de service de démarrage", {
            'classes': ('collapse',),
            'fields': ("not_osd_cst", "not_osd_date_accr", "not_osd_conf", "not_osd_obs",)
        }),
        ("Existence et exhaustivité de l'archivage des documents", {
            'classes': ('collapse',),
            'fields': ("ext_exh_arch_doc_exi", "ext_exh_arch_doc_exh", "ext_exh_arch_doc_obs",)
        }),
    )

    # Bouton pour exporter en Excel
    @button(label="Exporter en Excel", html_attrs={'style': 'background-color:#00AA00;color:black'})
    def export_to_excel(self, request):
        file = ExcelFile("GAG-Guide de contrôle à postériori.xlsx", "GAG_2", 7, 1,'Gag')
        workbook = file.create_excel_file()
        # Créer une réponse HTTP pour envoyer le fichier Excel
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Gré_à_gré.xlsx'

        # Sauvegarder le fichier Excel dans la réponse
        workbook.save(response)
        return response  


@admin.register(Pso)
class PsoAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super().__init__(model, admin_site)

    fieldsets = (
        ("Généralites", {
            'classes': ('collapse',),
            'fields': ("agent_cont", "date_contr", "ministere", "ac", "pers_res", "imputation", "num_aoo", "objet", "nat_oper", "nat_oper_obs")
        }),
        ("PSPM", {
            'classes': ('collapse',),
            'fields': ("pspm_exist",)
        }),
        ("Publication du PSPM", {
            'classes': ('collapse',),
            'fields': ("pub_pspm_cst", "pub_pspm_obs",)
        }),
        ("Inscription de l’opération au PSPM et respect du PSPM", {
            'classes': ('collapse',),
            'fields': ("ope_insc_pspm", "ope_insc_pspm_obs",)
        }),
        ("Montant de la dotation / du Crédit", {
            'classes': ('collapse',),
            'fields': ("mt_dot",)
        }),
        ("Situation d'exécution de la ligne budgetaire avant passation", {
            'classes': ('collapse',),
            'fields': ("st_exec_avt_pass_mt",)
        }),
        ("Montant de l'Estimation", {
            'classes': ('collapse',),
            'fields': ("mt_est",)
        }),
        ("Opération réservée aux PME", {
            'classes': ('collapse',),
            'fields': ("ope_res_pme", "ope_res_pme_obs",)
        }),
        ("Examen et validation du DAO par la DGMP", {
            'classes': ('collapse',),
            'fields': ("exam_val_dao_dgmp_cst", "exam_val_dao_dgmp_dte_dao_dgmp", "exam_val_dao_dgmp_dte_dao_dgmp_obs")
        }),
        ("Exigence du quitus de non redevance dans le DAO ", {
            'classes': ('collapse',),
            'fields': ("exg_quitus_dao_cst", "exg_quitus_dao_obs",)
        }),
        ("Publication de l'avis d'appel d'offres dans le BOMP", {
            'classes': ('collapse',),
            'fields': ("pub_aao_bomp_cst", "pub_aao_bomp_date", "pub_aao_bomp_no_bomp", "pub_aao_bomp_duree", "pub_aao_bomp_obs")
        }),
        ("Existence d’une liste de retrait du dossier de consultation ", {
            'classes': ('collapse',),
            'fields': ("exist_lst_rtr_dao_cst", "exist_lst_rtr_dao_nb_dos_ret", "exist_lst_rtr_dao_obs", )
        }),
        ("Convocation de la COPE", {
            'classes': ('collapse',),
            'fields': ("conv_cojo_cst", "conv_cojo_obs", )
        }),
        ("Existence de la COPE", {
            'classes': ('collapse',),
            'fields': ("exist_cojo_cst", "exist_cojo_obs", )
        }),
        ("Composition de la COPE", {
            'classes': ('collapse',),
            'fields': ("comp_cojo_conf", "comp_cojo_obs", )
        }),
        ("Existence d’une liste de présence des membres de la COPE", {
            'classes': ('collapse',),
            'fields': ("exist_lst_prs_mb_cojo_cst", "exist_lst_prs_mb_cojo_obs", )
        }),
        ("Existence des mandats des répresentants des membres de la COPE", {
            'classes': ('collapse',),
            'fields': ("exist_mdt_rep_mb_cojo_cst", "exist_mdt_rep_mb_cojo_obs", )
        }),
        ("Respect du quorum au niveau de la COPE", {
            'classes': ('collapse',),
            'fields': ("res_qr_nv_cojo_cst", "res_qr_nv_cojo_obs", )
        }),
        ("Existence d’une liste de dépôt des plis", {
            'classes': ('collapse',),
            'fields': ("exist_lst_dpt_plis_cst", "exist_lst_dpt_plis_nb_plis_dep", "exist_lst_dpt_plis_conf_lst_dpt_lst_rtr", "exist_lst_dpt_plis_obs",)
        }),
        ("Respect des dates et heures limites de dépôt des plis ", {
            'classes': ('collapse',),
            'fields': ("resp_date_heure_lmt_dep_plis_cst", "resp_date_heure_lmt_dep_plis_obs",)
        }),
        ("Respect des dates et heures d'ouverture des plis", {
            'classes': ('collapse',),
            'fields': ("resp_date_heure_lmt_ouv_cst", "resp_date_heure_lmt_ouv_obs",)
        }),
        ("Existence d’une liste de présence des soumissionnaires", {
            'classes': ('collapse',),
            'fields': ("ext_lst_prsc_sum_cst", "ext_lst_prsc_sum_obs",)
        }),
        ("Existence du procès-verbal d’ouverture des plis", {
            'classes': ('collapse',),
            'fields': ("ext_pv_ouv_plis", "ext_pv_ouv_plis_obs",)
        }),
        ("Existence et conformité du rapport d’analyse des offres", {
            'classes': ('collapse',),
            'fields': ("ext_rap_ana", "ext_rap_ana_obs",)
        }),
        ("Conformité de la COPE au jugement", {
            'classes': ('collapse',),
            'fields': ("conf_cojo_jug_cst", "conf_cojo_jug_obs",)
        }),
        ("Existence du procès-verbal de jugement des offres", {
            'classes': ('collapse',),
            'fields': ("ext_pv_jug_off_exst_pv", "ext_pv_jug_off_exst_pv_obs",)
        }),
        ("Respect du délai imparti à la COPE pour ses travaux", {
            'classes': ('collapse',),
            'fields': ("resp_del_imp_cojo_trv_cst", "resp_del_imp_cojo_trv_dta_ouv", "resp_del_imp_cojo_trv_dta_jug", "resp_del_imp_cojo_trv_dta_dern_jug", "resp_del_imp_cojo_trv_nb_jug", "resp_del_imp_cojo_trv_del_trv", "resp_del_imp_cojo_trv_obs")
        }),
        ("Publication des résultats de la COPE par la DGMP", {
            'classes': ('collapse',),
            'fields': ("pub_res_cojo_dgmp_cst", "pub_res_cojo_dgmp_date_pub", "pub_res_cojo_dgmp_no_bomp", "pub_res_cojo_dgmp_obs",)
        }),
        ("Notification des résultats aux attributaires", {
            'classes': ('collapse',),
            'fields': ("not_res_att_cst", "not_res_att_date", "not_res_att_obs",)
        }),
        ("Information des soumissionnaires non retenus", {
            'classes': ('collapse',),
            'fields': ("inf_soum_nn_ret_res_cst", "inf_soum_nn_ret_res_obs",)
        }),
        ("Attributaire(s)", {
            'classes': ('collapse',),
            'fields': ("att_rs_soc", "att_ncc_att", "att_lot", "att_mt", "att_obs",)
        }),
        ("Respect du délai de recours éventuel", {
            'classes': ('collapse',),
            'fields': ("res_del_rec_evt_cst", "res_del_rec_evt_nb_rec", "res_del_rec_evt_obs", )
        }),
        ("Existence un marché", {
            'classes': ('collapse',),
            'fields': ("ext_mar_cst", "ext_mar_obs",)
        }),
        ("Conformité du contenu du marché", {
            'classes': ('collapse',),
            'fields': ("conf_cont_mar_cst", "conf_cont_mar_obs",)
        }),
        ("Signature du marché par attributaire", {
            'classes': ('collapse',),
            'fields': ("sig_mar_att_cst", "sig_mar_att_date", "sig_mar_att_obs",)
        }),
        ("Examen préalable à l'approbation", {
            'classes': ('collapse',),
            'fields': ("exm_pre_app_cst", "exm_pre_app_obs",)
        }),
        ("Signature du marché par Autorité Contractante ou approbation", {
            'classes': ('collapse',),
            'fields': ("sig_mar_ac_cst", "sig_mar_ac_date", "sig_mar_ac_obs",)
        }),
        ("Autorité approbatrice", {
            'classes': ('collapse',),
            'fields': ("sig_aco_cst", "sig_aco_obs",)
        }),
        ("Numérotation du marché", {
            'classes': ('collapse',),
            'fields': ("num_mar_cst", "num_mar_date_num", "num_mar_nom", "num_mar_obs",)
        }),
        ("Conformité du Numéro du marché", {
            'classes': ('collapse',),
            'fields': ("conf_num_mar_cst", "conf_num_mar_obs",)
        }),
        ("Montant du marché", {
            'classes': ('collapse',),
            'fields': ("mt_mar",)
        }),
        ("Ecart entre montant estimatif et montant attribué", {
            'classes': ('collapse',),
            'fields': ("ect_mte_mta",)
        }),
        ("Production des pièces fiscales et sociales par attributaire", {
            'classes': ('collapse',),
            'fields': ("prd_pc_fic_soc_att_cst", "prd_pc_fic_soc_att_obs",)
        }),
        ("Notification de l'approbation du marché au titulaire", {
            'classes': ('collapse',),
            'fields': ("not_app_mar_ttl", "not_app_mar_ttl_date_rec", "not_app_mar_ttl_obs",)
        }),
        ("Enregistrement du marché", {
            'classes': ('collapse',),
            'fields': ("enr_mar_cst", "enr_mar_obs", )
        }),
        ("Transmission de 02 exemplaires du contrat à la DGMP", {
            'classes': ('collapse',),
            'fields': ("trans_dx_exp_ctr_dgmp_cst", "trans_dx_exp_ctr_dgmp_obs", )
        }),
        ("Notification de l'ordre de service de démarrage", {
            'classes': ('collapse',),
            'fields': ("not_osd_cst", "not_osd_date_accr", "not_osd_conf", "not_osd_obs",)
        }),
        ("Existence et exhaustivité de l'archivage des documents", {
            'classes': ('collapse',),
            'fields': ("ext_exh_arch_doc_exi", "ext_exh_arch_doc_exh", "ext_exh_arch_doc_obs",)
        }),
    )

    # Bouton pour exporter en Excel
    @button(label="Exporter en Excel", html_attrs={'style': 'background-color:#00AA00;color:black'})
    def export_to_excel(self, request):
        file = ExcelFile("PSO-Guide contrôle a posteriori.xlsx", 
                         "GUIDE_PSO_2", 
                         7, 
                         1, 
                         'Pso',
                         "DATA_PSO",  
                         4, 
                         1)
        workbook = file.create_excel_file()
        # Créer une réponse HTTP pour envoyer le fichier Excel
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Procédure_simplifiée_ouverte.xlsx'

        # Sauvegarder le fichier Excel dans la réponse
        workbook.save(response)
        return response  


@admin.register(Psl)
class PslAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super().__init__(model, admin_site)

    fieldsets = (
        ("Généralites", {
            'classes': ('collapse',),
            'fields': ("agent_cont", "date_contr", "ministere", "ac", "pers_res", "imputation", "num_ope", "objet", "nat_oper", "nat_oper_obs")
        }),
        ("PSPM", {
            'classes': ('collapse',),
            'fields': ("pspm_exist",)
        }),
        ("Publication du PSPM", {
            'classes': ('collapse',),
            'fields': ("pub_pspm_cst", "pub_pspm_obs",)
        }),
        ("Inscription de l’opération au PSPM et respect du PSPM", {
            'classes': ('collapse',),
            'fields': ("ope_insc_pspm", "ope_insc_pspm_obs",)
        }),
        ("Montant de la dotation / du Crédit", {
            'classes': ('collapse',),
            'fields': ("mt_dot",)
        }),
        ("Situation d'exécution de la ligne budgetaire avant passation", {
            'classes': ('collapse',),
            'fields': ("st_exec_avt_pass_mt",)
        }),
        ("Montant de l'Estimation", {
            'classes': ('collapse',),
            'fields': ("mt_est",)
        }),
        ("Opération réservée aux PME", {
            'classes': ('collapse',),
            'fields': ("ope_res_pme", "ope_res_pme_obs",)
        }),
        ("Examen et validation du DAO par la DGMP", {
            'classes': ('collapse',),
            'fields': ("exam_val_dao_dgmp_cst", "exam_val_dao_dgmp_dte_dao_dgmp", "exam_val_dao_dgmp_dte_dao_dgmp_obs")
        }),
        ("Exigence du quitus de non redevance dans le DAO ", {
            'classes': ('collapse',),
            'fields': ("exg_quitus_dao_cst", "exg_quitus_dao_obs",)
        }),
        ("Liste des entreprises consultées (N°CC-Libellé entreprise)", {
            'classes': ('collapse',),
            'fields': ("lst_ent_cslt_lot", "lst_ent_cslt_nb_ent", "lst_ent_cslt_ref_acc_pr_cslt_mn_cq_ent", "lst_ent_cslt_ent_1", "lst_ent_cslt_ent_2", "lst_ent_cslt_ent_3", "lst_ent_cslt_ent_4", "lst_ent_cslt_ent_5")
        }),
        ("Manifestation effective de l'intérêt des entreprises sollicitées à participer à la compétition", {
            'classes': ('collapse',),
            'fields': ("man_eff_int_ent_sol_part_comp_cst", "man_eff_int_ent_sol_part_comp_obs", )
        }),
        ("Respect du délai de dépôt de la lettre d'intention", {
            'classes': ('collapse',),
            'fields': ("res_del_dep_let_int_cst", "res_del_dep_let_int_obs", )
        }),
        ("Existence d’une liste de retrait du dossier de consultation", {
            'classes': ('collapse',),
            'fields': ("ext_lst_ret_dos_con_cst", "ext_lst_ret_dos_con_nb_dos_ret", "ext_lst_ret_dos_con_obs",)
        }),

        ("Convocation de la COPE", {
            'classes': ('collapse',),
            'fields': ("conv_cojo_cst", "conv_cojo_obs", )
        }),
        ("Existence de la COPE", {
            'classes': ('collapse',),
            'fields': ("exist_cojo_cst", "exist_cojo_obs", )
        }),
        ("Composition de la COPE", {
            'classes': ('collapse',),
            'fields': ("comp_cojo_conf", "comp_cojo_obs", )
        }),
        ("Existence d’une liste de présence des membres de la COPE", {
            'classes': ('collapse',),
            'fields': ("exist_lst_prs_mb_cojo_cst", "exist_lst_prs_mb_cojo_obs", )
        }),
        ("Existence des mandats des répresentants des membres de la COPE", {
            'classes': ('collapse',),
            'fields': ("exist_mdt_rep_mb_cojo_cst", "exist_mdt_rep_mb_cojo_obs", )
        }),
        ("Respect du quorum au niveau de la COPE", {
            'classes': ('collapse',),
            'fields': ("res_qr_nv_cojo_cst", "res_qr_nv_cojo_obs", )
        }),
        ("Existence d’une liste de dépôt des plis", {
            'classes': ('collapse',),
            'fields': ("exist_lst_dpt_plis_cst", "exist_lst_dpt_plis_nb_plis_dep", "exist_lst_dpt_plis_conf_lst_dpt_lst_rtr", "exist_lst_dpt_plis_obs",)
        }),
        ("Respect des dates et heures limites de dépôt des plis ", {
            'classes': ('collapse',),
            'fields': ("resp_date_heure_lmt_dep_plis_cst", "resp_date_heure_lmt_dep_plis_obs",)
        }),
        ("Respect des dates et heures d'ouverture des plis", {
            'classes': ('collapse',),
            'fields': ("resp_date_heure_lmt_ouv_cst", "resp_date_heure_lmt_ouv_obs",)
        }),
        ("Existence d’une liste de présence des soumissionnaires", {
            'classes': ('collapse',),
            'fields': ("ext_lst_prsc_sum_cst", "ext_lst_prsc_sum_obs",)
        }),
        ("Existence du procès-verbal d’ouverture des plis", {
            'classes': ('collapse',),
            'fields': ("ext_pv_ouv_plis", "ext_pv_ouv_plis_obs",)
        }),
        ("Existence et conformité du rapport d’analyse des offres", {
            'classes': ('collapse',),
            'fields': ("ext_rap_ana", "ext_rap_ana_obs",)
        }),
        ("Conformité de la COPE au jugement", {
            'classes': ('collapse',),
            'fields': ("conf_cojo_jug_cst", "conf_cojo_jug_obs",)
        }),
        ("Existence du procès-verbal de jugement des offres", {
            'classes': ('collapse',),
            'fields': ("ext_pv_jug_off_exst_pv", "ext_pv_jug_off_exst_pv_obs",)
        }),
        ("Respect du délai imparti à la COPE pour ses travaux", {
            'classes': ('collapse',),
            'fields': ("resp_del_imp_cojo_trv_cst", "resp_del_imp_cojo_trv_dta_ouv", "resp_del_imp_cojo_trv_dta_jug", "resp_del_imp_cojo_trv_dta_dern_jug", "resp_del_imp_cojo_trv_nb_jug", "resp_del_imp_cojo_trv_del_trv", "resp_del_imp_cojo_trv_obs",)
        }),
        ("Liste des soumissionnaires & montant de l'offre", {
            'classes': ('collapse',),
            'fields': ("lst_soum_mt_off_lot", "lst_soum_mt_off_nb_soum", "lst_soum_mt_off_soum_1_ncc_nom_ent", "lst_soum_mt_off_soum_1_mt_off", "lst_soum_mt_off_soum_2_ncc_nom_ent", "lst_soum_mt_off_soum_2_mt_off", "lst_soum_mt_off_soum_3_ncc_nom_ent", "lst_soum_mt_off_soum_3_mt_off", "lst_soum_mt_off_soum_4_ncc_nom_ent", "lst_soum_mt_off_soum_4_mt_off", "lst_soum_mt_off_soum_5_ncc_nom_ent", "lst_soum_mt_off_soum_5_mt_off", )
        }),
        ("Notification des résultats aux attributaires", {
            'classes': ('collapse',),
            'fields': ("not_res_att_cst", "not_res_att_date", "not_res_att_obs",)
        }),
        ("Information des soumissionnaires non retenus", {
            'classes': ('collapse',),
            'fields': ("inf_soum_nn_ret_res_cst", "inf_soum_nn_ret_res_obs",)
        }),
        ("Attributaire(s)", {
            'classes': ('collapse',),
            'fields': ("att_rs_soc", "att_ncc_att", "att_lot", "att_mt", "att_obs",)
        }),
        ("Respect du délai de recours éventuel", {
            'classes': ('collapse',),
            'fields': ("res_del_rec_evt_cst", "res_del_rec_evt_nb_rec", "res_del_rec_evt_obs", )
        }),
        ("Existence un marché", {
            'classes': ('collapse',),
            'fields': ("ext_mar_cst", "ext_mar_obs",)
        }),
        ("Conformité du contenu du marché", {
            'classes': ('collapse',),
            'fields': ("conf_cont_mar_cst", "conf_cont_mar_obs",)
        }),
        ("Signature du marché par attributaire", {
            'classes': ('collapse',),
            'fields': ("sig_mar_att_cst", "sig_mar_att_date", "sig_mar_att_obs",)
        }),
        ("Examen préalable à l'approbation", {
            'classes': ('collapse',),
            'fields': ("exm_pre_app_cst", "exm_pre_app_obs",)
        }),
        ("Signature du marché par Autorité Contractante ou approbation", {
            'classes': ('collapse',),
            'fields': ("sig_mar_ac_cst", "sig_mar_ac_date", "sig_mar_ac_obs",)
        }),
        ("Autorité approbatrice", {
            'classes': ('collapse',),
            'fields': ("sig_aco_cst", "sig_aco_obs",)
        }),
        ("Numérotation du marché", {
            'classes': ('collapse',),
            'fields': ("num_mar_cst", "num_mar_date_num", "num_mar_num", "num_mar_obs",)
        }),
        ("Conformité du Numéro du marché", {
            'classes': ('collapse',),
            'fields': ("conf_num_mar_cst", "conf_num_mar_obs",)
        }),
        ("Montant du marché", {
            'classes': ('collapse',),
            'fields': ("mt_mar",)
        }),
        ("Ecart entre montant estimatif et montant attribué", {
            'classes': ('collapse',),
            'fields': ("ect_mte_mta",)
        }),
        ("Production des pièces fiscales et sociales par attributaire", {
            'classes': ('collapse',),
            'fields': ("prd_pc_fic_soc_att_cst", "prd_pc_fic_soc_att_obs",)
        }),
        ("Notification de l'approbation du marché au titulaire", {
            'classes': ('collapse',),
            'fields': ("not_app_mar_ttl", "not_app_mar_ttl_date_rec", "not_app_mar_ttl_obs",)
        }),
        ("Enregistrement du marché", {
            'classes': ('collapse',),
            'fields': ("enr_mar_cst", "enr_mar_obs", )
        }),
        ("Transmission de 02 exemplaires du contrat à la DGMP", {
            'classes': ('collapse',),
            'fields': ("trans_dx_exp_ctr_dgmp_cst", "trans_dx_exp_ctr_dgmp_obs", )
        }),
        ("Notification de l'ordre de service de démarrage", {
            'classes': ('collapse',),
            'fields': ("not_osd_cst", "not_osd_date_accr", "not_osd_conf", "not_osd_obs",)
        }),
        ("Existence et exhaustivité de l'archivage des documents", {
            'classes': ('collapse',),
            'fields': ("ext_exh_arch_doc_exi", "ext_exh_arch_doc_exh", "ext_exh_arch_doc_obs",)
        }),
    )

    # Bouton pour exporter en Excel
    @button(label="Exporter en Excel", html_attrs={'style': 'background-color:#00AA00;color:black'})
    def export_to_excel(self, request):
        file = ExcelFile("PSL-Guide contrôle a posteriori.xlsx", 
                         "GUIDE_contrôle_PSL_2", 
                         7, 
                         1, 
                         'Psl',
                         "DATA_PSL_2",
                         4, 
                         1)
        workbook = file.create_excel_file()
        # Créer une réponse HTTP pour envoyer le fichier Excel
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Procédure_simplifiée_limite.xlsx'

        # Sauvegarder le fichier Excel dans la réponse
        workbook.save(response)
        return response 


@admin.register(Psc)
class PscAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super().__init__(model, admin_site)
    
    fieldsets = (
        ("Généralites", {
            'classes': ('collapse',),
            'fields': ("agent_cont", "date_contr", "ministere", "ac", "pers_res", "imputation", "num_ope", "objet", "nat_oper", "nat_oper_obs")
        }),
        ("PSPM", {
            'classes': ('collapse',),
            'fields': ("pspm_exist",)
        }),
        ("Publication du PSPM", {
            'classes': ('collapse',),
            'fields': ("pub_pspm_cst", "pub_pspm_obs",)
        }),
        ("Inscription de l’opération au PSPM et respect du PSPM", {
            'classes': ('collapse',),
            'fields': ("ope_insc_pspm", "ope_insc_pspm_obs",)
        }),
        ("Montant de la dotation / du Crédit", {
            'classes': ('collapse',),
            'fields': ("mt_dot",)
        }),
        ("Situation d'exécution de la ligne budgetaire avant passation", {
            'classes': ('collapse',),
            'fields': ("st_exec_avt_pass_mt",)
        }),
        ("Montant de l'Estimation", {
            'classes': ('collapse',),
            'fields': ("mt_est",)
        }),
        ("Opération réservée aux PME", {
            'classes': ('collapse',),
            'fields': ("ope_res_pme", "ope_res_pme_obs",)
        }),
        ("Formulaire de demande de cotation", {
            'classes': ('collapse',),
            'fields': ("form_dem_cot_conf_mod_elb_dgmp", "form_dem_cot_dte_trans_form", "form_dem_cot_obs", )
        }),
        ("Liste des entreprises consultées & montant des offres (N°CC-Libellé entreprise)", {
            'classes': ('collapse',),
            'fields': ("lst_ent_cslt_nb_ent", "lst_ent_cslt_ref_acc_pr_cslt_mn_cq_ent", "lst_ent_cslt_ent_1_ncc_nom", "lst_ent_cslt_ent_1_mtt", "lst_ent_cslt_ent_2_ncc_nom", "lst_ent_cslt_ent_2_mtt", "lst_ent_cslt_ent_3_ncc_nom", "lst_ent_cslt_ent_3_mtt"), 
        }),
        ("formulaire de sélection", {
            'classes': ('collapse',),
            'fields': ("form_sel_ext", "form_sel_conf_mod_dgmp", "form_sel_obs",)
        }),
        ("Date et signature du formulaire de selection", {
            'classes': ('collapse',),
            'fields': ("dte_sig_form_sel_sig", "dte_sig_form_sel_dte", "dte_sig_form_sel_qlte_sig", "dte_sig_form_sel_obs",)
        }),
        ("Attributaire(s)", {
            'classes': ('collapse',),
            'fields': ("att_lot", "att_rs_soc", "att_ncc_att", "att_mt", "att_obs", )
        }),
        ("Ecart entre montant estimatif et montant attribué", {
            'classes': ('collapse',),
            'fields': ("ect_mte_mta",)
        }),
        ("Notification de l'attribution au (x) soumissionnaire (s) retenu (s)", {
            'classes': ('collapse',),
            'fields': ("not_att_soum_ret_cst", "not_att_soum_ret_date", "not_att_soum_ret_obs", )
        }),
        ("Information des soumissionnaires non retenus", {
            'classes': ('collapse',),
            'fields': ("inf_soum_nn_ret_cst", "inf_soum_nn_ret_obs",)
        }),
        ("Notification de l'ordre de service de démarrage", {
            'classes': ('collapse',),
            'fields': ("not_osd_cst", "not_osd_date_accr", "not_osd_obs",)
        }),
        ("Existence et exhaustivité de l'archivage des documents", {
            'classes': ('collapse',),
            'fields': ("ext_exh_arch_doc_exi", "ext_exh_arch_doc_exh", "ext_exh_arch_doc_obs",)
        }),
    )

    # Bouton pour exporter en Excel
    @button(label="Exporter en Excel", html_attrs={'style': 'background-color:#00AA00;color:black'})
    def export_to_excel(self, request):
        file = ExcelFile("PSC-Guide évaluation des opérations.xlsx", 
                         "GUIDE_contrôle_PSC_2", 
                         7, 
                         1, 
                         'Psc',
                         "DATA_PSC_2",
                         4, 
                         1)
        workbook = file.create_excel_file()
        # Créer une réponse HTTP pour envoyer le fichier Excel
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Procédure_simplifiée_cotation.xlsx'

        # Sauvegarder le fichier Excel dans la réponse
        workbook.save(response)
        return response 


@admin.register(Psd)
class PsdAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super().__init__(model, admin_site)

    # Bouton pour exporter en Excel
    @button(label="Exporter en Excel", html_attrs={'style': 'background-color:#00AA00;color:black'})
    def export_to_excel(self, request):
        file = ExcelFile("PSD-Guide évaluation des opérations.xlsx", 
                         "GUIDE_contrôle_PSD_2", 
                         7, 
                         1, 
                         'Psd',
                         "DATA_PSD_2",
                         4, 
                         1)
        workbook = file.create_excel_file()
        # Créer une réponse HTTP pour envoyer le fichier Excel
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Procédure_simplifiée_entente_directe.xlsx'

        # Sauvegarder le fichier Excel dans la réponse
        workbook.save(response)
        return response 
    
    fieldsets = (
        ("Généralites", {
            'classes': ('collapse',),
            'fields': ("agent_cont", "date_contr", "ministere", "ac", "pers_res", "imputation", "objet", "nat_oper", "nat_oper_obs")
        }),
        ("Montant de la dotation / du Crédit", {
            'classes': ('collapse',),
            'fields': ("mt_dot",)
        }),
        ("Situation d'exécution de la ligne budgetaire avant passation", {
            'classes': ('collapse',),
            'fields': ("st_exec_avt_pass_mt",)
        }),
        ("PSPM", {
            'classes': ('collapse',),
            'fields': ("pspm_exist",)
        }),
        ("Publication du PSPM", {
            'classes': ('collapse',),
            'fields': ("pub_pspm_cst", "pub_pspm_obs",)
        }),
        ("Inscription de l’opération au PSPM et respect du PSPM", {
            'classes': ('collapse',),
            'fields': ("ope_insc_pspm", "ope_insc_pspm_obs",)
        }),
        
        ("Montant de l'Estimation", {
            'classes': ('collapse',),
            'fields': ("mt_est",)
        }),
        ("Opération réservée aux PME", {
            'classes': ('collapse',),
            'fields': ("ope_res_pme", "ope_res_pme_obs",)
        }),

        ("Date de commande", {
            'classes': ('collapse',),
            'fields': ("dte_commande", "dte_commande_obs", )
        }),
        
        ("Attributaire(s)", {
            'classes': ('collapse',),
            'fields': ("att_rs_soc", "att_ncc_att", "att_mt", "att_obs",)
        }),
        
        ("Ecart entre montant estimatif et montant attribué", {
            'classes': ('collapse',),
            'fields': ("ect_mte_mta", )
        }),
        
        ("Existence et exhaustivité de l'archivage des documents", {
            'classes': ('collapse',),
            'fields': ("ext_exh_arch_doc_exi", "ext_exh_arch_doc_exh", "ext_exh_arch_doc_obs",)
        }),
    )


























