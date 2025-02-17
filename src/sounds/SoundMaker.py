from common.ContextAware import ContextAware

class SoundMaker(ContextAware):

    def make_sound(self, prompt_dict: dict):
        """
        Generates sound based on the provided `prompt_dict`.
        
        Arguments:
        - `prompt_dict`(dict): A dictionary containing:
        * `positive_prompt_text` (str): Describes the sound or situation.
        * `negative_prompt_text` (optional str): Describes what should not be in the sound.        
        * `style_prompt_text` (optional str): Describes the desired sound style.
        * `style_prompt_sounds` (optional list of str): Sound URL strings showing the desired sound style. Useful for providing 
            the AI model with examples, especially for children's books where the same voices etc may appear in different situations.
        * `positive_prompt_sounds` (optional list of str): Image URL strings as positive examples.
        * `negative_prompt_sounds` (optional list of str): Image URL strings as negative examples.

        Returns:
            None or web browser playable url str of sound matching `prompt_dict`
        """
        raise Exception("Function not implemented")
