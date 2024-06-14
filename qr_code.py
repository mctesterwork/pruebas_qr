import pyqrcode
import png
import customtkinter

def main():
    customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"

    ctk = customtkinter.CTk()
    ctk.geometry("300x300")
    ctk.title("QR Code Generator")
    input = customtkinter.CTkEntry(ctk, placeholder_text="Introduce tu texto")
    input.place(relx=0.5, rely=0.3, anchor="center")

    label = customtkinter.CTkLabel(ctk, text="El texto es requerido", text_color="red")
    notificacion = customtkinter.CTkLabel(ctk, text="La imagen / QR se genero con exito!", text_color="green")

    selector = customtkinter.CTkComboBox(ctk, values=["PNG", "SVG"])
    selector.place(relx=0.5, rely=0.5, anchor="center")

    def generate():
        if input.get() == "":
            label.place(relx=0.5, rely=0.4, anchor="center")
            return
        else:
            label.place_forget()

        notificacion.place_forget()
        qr = pyqrcode.create(input.get())
        
        if selector.get() == "PNG":
            qr.png("qr.png", scale=8)
        else:
            qr.svg("qr.svg", scale=8)

        notificacion.place(relx=0.5, rely=0.8, anchor="center")
    
    button = customtkinter.CTkButton(ctk, text="Generar QR", command=generate)
    button.place(relx=0.5, rely=0.7, anchor="center")
    
    ctk.mainloop()

if __name__ == "__main__":
    main()