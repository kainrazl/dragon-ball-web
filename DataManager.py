from CharacterData import Character
from requests import get, exceptions

class DataManager:
    def __init__(self):
        pass

    def Get_Character_Info(self, character_name) -> Character:
        try:
            response = get(f"https://dragonball-api.com/api/characters?name={character_name}")
            if response.status_code == 200:
                character_list = response.json()#.get("data", [])
                if not character_list:
                    return {"error": f"No character found with name: {character_name}"}
                
                print(f"Character info: {character_list[0]}")  # Debugging line to check the first character data
                character_data = Character.model_validate(character_list[0])  # Assuming the first match is the desired character
                return character_data
            else:
                return {"error": f"Character not found: {response.content}"}
        except Exception as e:
            print(f"Error fetching character data: {e}")
            return {"error": "An error occurred while fetching character data"}
        
if __name__ == "__main__":
    data_manager = DataManager()
    print(data_manager.Get_Character_Info("Goku"))