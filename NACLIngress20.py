from NACLIngressCheck import NACLIngressCheck


class NACLIngress20(CheckPortIP):
    def __init__(self):
        super().__init__(check_id="CKV_NCP_230", port=20)


check = NACLIngress20()