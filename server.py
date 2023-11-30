from model import NavalBattleModel
import mesa

model_params = {
    "num_cruzador": mesa.visualization.Slider(
        "Quantidade inicial de navios cruzadores", 100, 10, 300
    ),

    "num_torpedeiro": mesa.visualization.Slider(
        "Quantidade inicial de torpedeiros", 100, 10, 300
    ),
    "num_morteiro": mesa.visualization.Slider(
        "Quantidade inicial de morteiros", 2, 1, 10
    ),
    "num_contra_torpedeiro": mesa.visualization.Slider(
        "Quantidade inicial de contra_torpedeiros", 2, 1, 10
    ),
    "num_contra_morteiro": mesa.visualization.Slider(
        "Quantidade inicial de contra morteiros", 20, 0, 100
    ),
    "width": 100, 
    "height": 100 
}


boats_colors = {
    "morteiro": "", 
    "contra_morteiro":"",  
    "torpedeiro": "" , 
    "contra_torpedeiro":"" 
}

def render(): 
    return 



canvas_element = mesa.visualization.CanvasGrid(render, 100, 100, 700, 700)
server = mesa.visualization.ModularServer(NavalBattleModel, [canvas_element], "CrazyNavalBattle", model_params)
