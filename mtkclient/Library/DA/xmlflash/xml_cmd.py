    def cmd_get_sys_property(self, key="DA.SLA", host_mem_offset: int = 0x7fe83c138700, length=0x200000):
        """
        <?xml version="1.0" encoding="utf-8"?>
        <da>
            <version>1.0</version>
            <command>CMD:GET-SYS-PROPERTY</command>
            <arg>
                <key>DA.SLA</key>
                <target_file>MEM://0x7fe83c138700:0x200000</target_file>
            </arg>
        </da>
        """
        # --- INFINIX OFFLINE BYPASS MODULE ---
        if key == "DA.SLA":
            print("[+] Infinix GT 20/30 Pro için Offline DA.SLA Bypass tetiklendi!")
            
            offline_policy = (
                '<?xml version="1.0" encoding="utf-8"?>\n'
                '<da_policy>\n'
                '    <sla_enabled>False</sla_enabled>\n'
                '    <daa_enabled>False</daa_enabled>\n'
                '    <auth_status>DISABLED</auth_status>\n'
                '</da_policy>\n'
            ).encode('utf-8')

            try:
                if hasattr(self, 'mtk') and hasattr(self.mtk, 'port') and self.mtk.port is not None:
                    self.mtk.port.write(offline_policy)
                    print("[+] Saxta Offline Siyasəti (SEC-POLICY) USB Portu ilə ötürüldü.")
                elif hasattr(self, 'mtk') and hasattr(self.mtk, 'daloader') and hasattr(self.mtk.daloader, 'write'):
                    self.mtk.daloader.write(host_mem_offset, offline_policy)
                    print("[+] Saxta Offline Siyasəti (SEC-POLICY) daloader.write ilə ötürüldü.")
            except Exception as e:
                print(f"[-] USB kanalına yazarkən xəta baş verdi: {e}")
        # --- INFINIX OFFLINE BYPASS MODULE END ---

        content = {
            "arg": [
                f"<key>{key}</key>",
                f"<target_file>MEM://{hex(host_mem_offset)}:{hex(length)}</target_file>"
            ]
        }
        cmd = self.create_cmd("GET-SYS-PROPERTY", content)
        return cmd

    def cmd_set_host_info(self, hostinfo: str = ""):
        """
        <?xml version="1.0" encoding="utf-8"?><da><version>1.0</version>
        <command>CMD:SET-HOST-INFO</command>
        <arg><info>20230901T234721</info></arg>
        """
        if hostinfo == "":
            current_date_and_time = datetime.datetime.now()
            hostinfo = current_date_and_time.strftime("%Y%m%dT%H%M%S")
        content = {
            "arg": [
                f"<info>{hostinfo}</info>",
            ]
        }
        cmd = self.create_cmd("SET-HOST-INFO", content)
        return cmd

    def cmd_get_downloaded_image_feedback(self, mem_offset: int = 0x2000000, mem_length: int = 0x20000):
        content = {
            "arg": [
                f"<target_file>MEM://{hex(mem_offset)}:{hex(mem_length)}</target_file>",
            ]
        }
        cmd = self.create_cmd("GET-DOWNLOADED-IMAGE-FEEDBACK", content)
        return cmd
