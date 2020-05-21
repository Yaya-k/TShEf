#####################################################################
# La fonction principal: pour lancer le projet(F5 pour compiler )
#####################################################################

from interface import*

if __name__ == "__main__":
    app = SampleApp()
    app.title("TShef Application")
    app.iconbitmap("healthy-food.ico")
    app.mainloop()
