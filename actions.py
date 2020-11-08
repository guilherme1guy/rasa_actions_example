from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, EventType

import ptvsd


class ActionTest(Action):

    def __init__(self) -> None:
        ptvsd.enable_attach(('0.0.0.0', 3000))

    def name(self):
        return "action_test"

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Seu teste funcionou!")

        return []

class ActionTelefone(FormAction):

    def name(self) -> Text:
        return "telefone_form"

    @staticmethod
    def required_slots(tracker):
        return ['telefone']
    
    def slot_mappings(self):
        return {
            'telefone': self.from_entity("telefone")
        }

    def submit(self, dispatcher: "CollectingDispatcher", tracker: "Tracker", domain: Dict[Text, Any]) -> List[EventType]:

        dispatcher.utter_message(f"Seu telefone é {tracker.slots['telefone']}")

        return []

