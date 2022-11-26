from dict import international_morse_code
from dict import internat_mors_cod_encod
from playsound import playsound


def prepare_text(input_data, mode='encode'):
    return_form = []
    if mode == 'encode':
        for char in input_data.upper().split():
            return_form.append(morse_encode(char))

        return return_form
    elif mode == 'decode':
        for char in input_data.split():
            return_form.append(morse_decode(char))
        if return_form[0] == 'None':
            return_form = None
        return return_form


def morse_encode(text):
    morse_code = internat_mors_cod_encod
    encoded = []
    for char in [*text]:
        if char in morse_code:
            encoded.append(morse_code[char])
    return encoded


def morse_decode(morse):
    morse_code = international_morse_code
    decoded = []
    if morse in morse_code:
        decoded.append(morse_code[morse])
    elif morse == '/':
        decoded.append(morse)
    elif len(decoded) == 0:
        return None
    return decoded


def play_dot():
    playsound('data/dot.mp3')


def play_dash():
    playsound('data/dash.mp3')

