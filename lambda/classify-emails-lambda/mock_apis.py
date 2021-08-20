import random

TRN_STATUSES = ['FAILED', 'INPROGRESS', 'INVALID','SUCCESSFUL']

def get_trasfer_status(trn_id):
    return TRN_STATUSES[random.randint(0, len(TRN_STATUSES)-1)]