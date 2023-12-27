from scapy.layers import l2


class Arp:
    @staticmethod
    def search(net):
        mac_list = []
        # ans : 응답
        # noans : 미응답
        ans, noans = l2.arping(net=net, timeout=1, verbose=True)

        for sent, received in ans.res:
            ip = received.psrc
            mac = received.hwsrc

            mac_list.append({
                'ip': ip,
                'mac': mac,
            })

        return mac_list

    @staticmethod
    def get_mac_by_ip(ip):
        mac = l2.getmacbyip(ip)
        return mac
