#CSV de teste
CSV_PATH = 'SMGPAT/queries/csv_query_test.csv'

#TRANSFERENCIAS

INCLUDE_TRANSFERENCE_BUTTON_NAME = 'BTNINCLUIR'
TRANSFERENCE_BUTTON_NAME = 'IMAGETRANSF'
INPUT_TEXT_AREA_TRANSFERENCE_ID = 'vTRANSFPATDESC'
PLAQUETA_REFERENCIA_ID = 'vPATPLAQUETA'
ORIGEN_REFERENCIA_ID = 'vTRANSFPATORGORIGID'
TRANSFERENCE_DESTINY_INPUT_ID = 'vTRANSFPATORGNDESTID'
CONFIRM_TRANSFERENCE_BUTTON_NAME = 'BTNCONFIRMAR'
CLOSE_TRANSFERENCE_CONFIRM_MODAL_NAME = 'VOLTAR'
CLOSE_TRANSFERENCE_CONFIRM_MODAL_CLASNAME = 'VOLTAR'
INCLUDE_ITEMS_FORM_ID = 2
INPUT_SEARCH_BY_PLAQUETA = '//*[@id="W0136TABLE1"]/tbody/tr[1]/td[2]/span/input[2]'
INPUT_PLAQUETA_ID = 'W0136vPATPLAQUETA'
INCLUDE_ITEM_BUTTON_NAME = 'W0136BUTTON1'
CLOSE_POPUP_MODULE_BTN_XPATH = '/html/body/form/p/table/tbody/tr/td/table/tbody/tr[2]/td/input[1]'
CLOSE_POPUP_MODULE_BTN_ID = 'gxp0_cls'
BACK_POPUP_TRANFERENCE_XPATH = '//*[@id="TABLE1"]/tbody/tr[2]/td/input[1]'
LAST_TRANFERENCE_NUMBER_ID = 'span_CTLTRANSFPATCODIGO_0001'
FINALIZE_TRANSFERENCE_BUTTON_NAME = 'vSTATUS_0001'
TRANSFERENCE_CODE_XPATH = '//*[@id="span_vTRANSFPATCODIGO"]'
TRANSFERENCE_INPUT_CODE_ID = 'vTRANSFPATCODIGO'
BACK_MODULE_BTN_NAME = 'VOLTAR'

# Item por paginação
GROUP_SIZE = 10

# Constantes para IDs dos campos de login
LOGIN_FIELDSET_ID = "CTLUSULOGIN"
PASSWORD_FIELDSET_ID = "CTLUSUSENHA"
BUTTOM_FORM_LOGIN_NAME = "BUTTON1"
BUTTOM_FORM_MODULE_ID = 'IMAGEMODULO_0002'

# Constantes para a tabela de resultados na tela inicial de incorporação de bens móveis
TABLE_RESULT_ID = 'GriddetalhesContainerTbl'
BUTTON_VIZUALIZER_NAME = 'vVISUALIZAR_'

HEADERS_QUERY_CSV = {
            "patplaqueta": '',
            "status": '',
            "organograma_name": '',
            "material_id": '',
            "material_name": '',
            "nota_fiscal": '',
            "serie_nota_fiscal": '',
            "incluido_por": '',
            "incluido_em": '',
            "modificado_por": '',
            "ultima_modificacao": '',  
        }

# Constantes para a descricao do item pesquisado
PATPLAQUETA_ID = 'span_PATPLAQUETA'
STATUS_ID = 'span_PATSITUACAO'
ORGANOGRAMA_NAME_ID = 'span_PATORGNADMNOME'
MATERIAL_ID = 'span_vMATGRUPOCODIGO'
MATERIAL_NAME_ID = 'span_MATERIALNOME'
NOTA_FISCAL_ID = 'span_PATNOTAFISCALNMR'
SERIE_NOTA_FISCAL_ID = 'span_PATNOTAFISCALSERIE'
NUMERO_EMPENHO_ID = 'span_W0378CTLPATRIMONIOLIQEMPENHONMR_0001'
ANO_EMPENHO_ID = 'span_W0378CTLPATRIMONIOLIQEMPENHOANO_0001'
INCLUIDO_POR_ID = 'span_PATINCLUIDOPORNOME'
INCLUIDO_EM_ID = 'span_PATINCLUIDOEM'
MODIFICADO_POR_ID = 'span_PATALTERADOPORNOME'
ULTIMA_MODIFICACAO_ID = 'span_PATINCLUIDOEM'

# Botoes ações dentro da vizualização / edição de item
RETURN_FORM_NAME = 'BTN_CANCEL'

# Constantes para buscas items por plaquetas
PLAQUETA_INIT_ID = 'vPATPLAQUETAINI'
PLAQUETA_FINAL_ID = 'vPATPLAQUETAFIN'
BUTTON_QUERY = 'BTNCONSULTAR'
ROW_QUERY_ID = 'GriddetalhesContainerRow_'

# Constantes botões de incorporação patrimonial
BUTTON_NAV_INCORPORATION_ID = 'ext-gen23'
BUTTON_NAV_ITEM_XPATH = '(//div[contains(@class, "x-menu-list-item")])[1]'


