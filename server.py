from model import NavalBattleModel
import mesa
from src.boat import BoatAgent
from src.ContraMorteiro import ContraMorteiro
from src.Morteiro import Morteiro


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
    "width": 35, 
    "height": 35 
}


boats_colors = {
    "morteiro": "", 
    "contra_morteiro":"",  
    "torpedeiro": "" , 
    "contra_torpedeiro":"" 
}

def render(agent): 
    if agent is None:
        return

    portrayal = {
        "Filled": "true",
        "Layer": 0,
        "text_color": "White",
    }

    agent_color = "azul"

    if type(agent) is BoatAgent:
        portrayal["Shape"] = f"./src/assets/navio.png"
    elif type(agent) is ContraMorteiro:
        portrayal["Shape"] = f"./src/assets/fumaca.png"
    elif type(agent) is Morteiro:
        portrayal["Shape"] = f"./src/assets/arma-de-morteiro.png"

    # make subtitle in canvas_elements
    # portrayal["life"] = (
    #     f"{agent.life:.2f}" if hasattr(agent, "life") else "∞"
    # )
    return portrayal


canvas_element = mesa.visualization.CanvasGrid(render, 35, 35, 700, 700)
server = mesa.visualization.ModularServer(NavalBattleModel, [canvas_element], "CrazyNavalBattle", model_params)
