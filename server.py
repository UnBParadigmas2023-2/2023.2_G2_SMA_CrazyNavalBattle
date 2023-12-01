from model import NavalBattleModel
from src.Affiliation import Affiliation
import mesa
from src.boat import BoatAgent
from src.Cruzador import Cruzador
from src.Torpedeiro import Torpedeiro
from src.ContraMorteiro import ContraMorteiro
from src.Morteiro import Morteiro
from src.ContraTorpedeiro import ContraTorpedeiro

model_params = {
    "num_cruzador_fla": mesa.visualization.Slider(
        name="Número de cruzadores do Flamengo",
        min_value=0,
        max_value=10,
        step=1,
        value=1,
    ),
    "num_torpedeiro_fla": mesa.visualization.Slider(
        name="Número de torpedeiros do Flamengo",
        min_value=0,
        max_value=10,
        step=1,
        value=1,
    ),
    "num_morteiro_fla": mesa.visualization.Slider(
        name="Número de morteiros do Flamengo",
        min_value=0,
        max_value=10,
        step=1,
        value=1,
    ),
    "num_contra_torpedeiro_fla": mesa.visualization.Slider(
        name="Número de contra torpedeiros do Flamengo",
        min_value=0,
        max_value=10,
        step=1,
        value=1,
    ),
    "num_contra_morteiro_fla": mesa.visualization.Slider(
        name="Número de contra morteiros do Flamengo",
        min_value=0,
        max_value=10,
        step=1,
        value=1,
    ),
    "num_cruzador_flu": mesa.visualization.Slider(
        name="Número de cruzadores do Fluminense",
        min_value=0,
        max_value=10,
        step=1,
        value=1,
    ),
    "num_torpedeiro_flu":mesa.visualization.Slider(
        name="Número de torpedeiros do Fluminense",
        min_value=0,
        max_value=10,
        step=1,
        value=1,
    ),
    "num_morteiro_flu": mesa.visualization.Slider(
        name="Número de morteiros do Fluminense",
        min_value=0,
        max_value=10,
        step=1,
        value=1,
    ),
    "num_contra_torpedeiro_flu": mesa.visualization.Slider(
        name="Número de contra torpedeiros do Fluminense",
        min_value=0,
        max_value=10,
        step=1,
        value=1,
    ),
    "num_contra_morteiro_flu": mesa.visualization.Slider(
        name="Número de contra morteiros do Fluminense",
        min_value=0,
        max_value=10,
        step=1,
        value=1,
    ),
    "width": 15,
    "height": 15
}

def render(): 
    return 

def enemy_ally_quantity(model):
    fla = [r for r in model.schedule.agents if Affiliation.FLAMENGO == r._affiliation]
    flu = [p for p in model.schedule.agents if Affiliation.FLUMINENSE == p._affiliation]
    return f"Flamengo: {len(fla)}<br>Fluminense: {len(flu)}"

def design_model(agent):
    if agent is None:
        return

    portrayal = {
        "Filled": "true",
        "Layer": 0,
        "text_color": "White",
    }

    time = "flamengo" if agent._affiliation == Affiliation.FLAMENGO else "fluminense"

    if type(agent) is Torpedeiro:
        portrayal["Shape"] = f"./src/assets/{time}/torpedeiro_{time}.png"
    elif type(agent) is ContraTorpedeiro:
        portrayal["Shape"] = f"./src/assets/{time}/contratorpedeiro_{time}.png"
    elif type(agent) is Cruzador:
        portrayal["Shape"] = f"./src/assets/{time}/navio_{time}.png"
    elif type(agent) is ContraMorteiro:
        portrayal["Shape"] = f"./src/assets/{time}/contramorteiro_{time}.png"
    elif type(agent) is Morteiro:
        portrayal["Shape"] = f"./src/assets/{time}/morteiro_{time}.png"
    # make subtitle in canvas_elements
    portrayal["life"] = (
        f"{agent.life:.2f}" if hasattr(agent, "life") else "∞"
    )
    return portrayal


canvas_elements = mesa.visualization.CanvasGrid(design_model, 15, 15, 1000, 1000)
 
server = mesa.visualization.ModularServer(
    NavalBattleModel,
    [
        canvas_elements,
        enemy_ally_quantity,
    ],
    "Batalha Naval",
    model_params,
)

server.description = (
    "Modelo de simulação de uma batalha naval entre os times Flamengo e Fluminense."
)