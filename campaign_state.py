import pyautogui as pag
import time

####IMAGE MACROS
victory_screen = 'images/victory.png'
defeat_screen = 'images/defeat.png'
campaign_begin_button = 'images/begin_button.png'
kt_challenge_button = 'images/kt_challenge_button.png'
####

def is_on_screen(target):
    """
    Takes a filepath to image as arguement
    Returns True if image is present on screen
    Returns False otherwise
    """
    return pag.locateOnScreen(target, confidence = 0.8)


def click_state(target):
    """
    Takes a filepath to image as arguement
    Returns nothing
    """
    pag.click(pag.locateCenterOnScreen(target, confidence = 0.8))


def wait_state():
    """
    Takes no arguement
    Handles waiting between click events
    Returns 0 if battle was successfuly compelted
    Returns -1 if wait stage stuck for >65 seconds
    """   
    print("Looking for state transition criteria...")
    time.sleep(2)  #Handles potential lag between screen transitions

    for _ in range(13): #Waiting 65 seconds is sufficient for battle to complete
        if is_on_screen(victory_screen):
            click_state(victory_screen)
            return 1
        elif is_on_screen(defeat_screen):
            click_state(defeat_screen)
            return 2
        elif is_on_screen(campaign_begin_button):
            print("Begin button found")
            click_state(campaign_begin_button)
       
        time.sleep(5) 

    #Exit with an error code if wait_stage is stuck for >65 seconds
    return -1 #


def identify_start_state():
    """
    Takes no argument
    Identifies initial state and the next state to enter
    Returns 0 if battle was succesffuly completed
    Returns -1 if unable to complete a battle
    """
    print("#####BATTLE_STATE_START#####")

    if is_on_screen(victory_screen):
        click_state(victory_screen)
        print("Identified victory screen")
        return 0
    elif is_on_screen(defeat_screen):
        click_state(defeat_screen)
        print("Identified defeat screen")
        return 0
    elif is_on_screen(campaign_begin_button):
        click_state(campaign_begin_button)
        print("Identified begin button. Entering wait state")
        return wait_state()
    elif is_on_screen(kt_challenge_button):
        click_state(kt_challenge_button)
        print("Identified challenge button. Entering wait state")
        return wait_state()


if __name__ == "__main__":
    state = identify_start_state()
    if state == 1:
        print("Battle won")
    elif state == 2:
        print("Battle lost")
    else:
        print("Battle state failure")
    print("#####BATTLE_STATE_END#####") 




