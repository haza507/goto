import flet as ft

tablero = [""] * 9
turno = "X"


def main(page: ft.Page):
    global turno

    page.title = "Juego de Gato"
    page.window.width = 350
    page.window.height = 450
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    estado = ft.Text(f"Turno: {turno}", size=20)

    botones = []

    def verificar():
        lineas = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6),
        ]

        for a, b, c in lineas:
            if tablero[a] and tablero[a] == tablero[b] == tablero[c]:
                estado.value = f"Ganó {tablero[a]}"
                for boton in botones:
                    boton.disabled = True
                page.update()
                return True

        if "" not in tablero:
            estado.value = "Empate"
            page.update()
            return True

        return False

    def click(e):
        global turno

        boton = e.control
        i = boton.data

        if tablero[i] == "":
            tablero[i] = turno
            boton.content.value = turno

            if not verificar():
                turno = "O" if turno == "X" else "X"
                estado.value = f"Turno: {turno}"

            page.update()

    def reiniciar(e):
        global turno

        turno = "X"

        for i in range(9):
            tablero[i] = ""
            botones[i].content.value = ""
            botones[i].disabled = False

        estado.value = "Turno: X"
        page.update()

    grid = ft.GridView(
        runs_count=3,
        max_extent=90,
        spacing=5,
        run_spacing=5,
        width=300,
        height=300,
    )

    for i in range(9):
        b = ft.ElevatedButton(
            content=ft.Text("", size=30),
            width=90,
            height=90,
            data=i,
            on_click=click,
        )

        botones.append(b)
        grid.controls.append(b)

    page.add(
        estado,
        grid,
        ft.ElevatedButton(
            content=ft.Text("Reiniciar"),
            on_click=reiniciar,
        ),
    )


ft.app(target=main)
