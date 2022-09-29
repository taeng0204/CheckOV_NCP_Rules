from NACLIngressCheck import NACLIngressCheck


class NACLIngress3389(CheckPortIP):
    def __init__(self):
        super().__init__(check_id="CKV_NCP_231", port=3389)


check = NACLIngress3389()