from NACLIngressCheck import NACLIngressCheck


class NACLIngress21(CheckPortIP):
    def __init__(self):
        super().__init__(check_id="CKV_NCP_229", port=21)


check = NACLIngress21()