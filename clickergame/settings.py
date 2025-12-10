import pygame

def draw_settings_menu(gameDisplay, grey, black, DrawText, rectangle, custom_color_mode=False, custom_r=0, custom_g=0, custom_b=0):
    """Draw the settings menu with color selection options"""
    # Settings menu background
    rectangle(gameDisplay, grey, 150, 100, 500, 400)
    DrawText("SETTINGS", black, grey, 400, 130, 40)
    
    if not custom_color_mode:
        # Color options (removed christmas from here to avoid type issues)
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (255, 255, 255), (0, 0, 0), (220, 20, 60)]
        color_names = ["Red", "Green", "Blue", "Yellow", "Orange", "White", "Black", "Christmas"]
        
        y_pos = 180
        for i, (color, name) in enumerate(zip(colors, color_names)):
            rectangle(gameDisplay, color, 200, y_pos, 30, 30)
            text_color = black if color not in ((0, 0, 0), (220, 20, 60)) else (255, 255, 255)
            DrawText(name, text_color, grey, 280, y_pos + 15, 16)
            y_pos += 35
        
        # Custom color button
        rectangle(gameDisplay, (128, 0, 128), 200, 455, 30, 30)
        DrawText("Custom", black, grey, 280, 470, 16)
        
        DrawText("Click color to select | Press ESC to close", black, grey, 400, 480, 14)
    else:
        # Custom color picker
        DrawText("CUSTOM COLOR PICKER", black, grey, 400, 150, 25)
        
        # RGB sliders
        DrawText(f"Red: {custom_r}", black, grey, 250, 200, 16)
        rectangle(gameDisplay, (200, 0, 0), 300, 195, 150, 20)
        DrawText(f"Green: {custom_g}", black, grey, 250, 250, 16)
        rectangle(gameDisplay, (0, 200, 0), 300, 245, 150, 20)
        DrawText(f"Blue: {custom_b}", black, grey, 250, 300, 16)
        rectangle(gameDisplay, (0, 0, 200), 300, 295, 150, 20)
        
        # Preview
        preview_color = (custom_r, custom_g, custom_b)
        rectangle(gameDisplay, preview_color, 200, 350, 100, 50)
        DrawText("Preview", black, grey, 250, 375, 14)
        
        # Buttons
        rectangle(gameDisplay, (0, 100, 0), 200, 420, 80, 30)
        DrawText("Apply", (255, 255, 255), (0, 100, 0), 240, 435, 14)
        
        rectangle(gameDisplay, (100, 0, 0), 320, 420, 80, 30)
        DrawText("Back", (255, 255, 255), (100, 0, 0), 360, 435, 14)

def handle_color_selection(x, y, colors_list):
    """Check if a color was clicked and return the selected color or None"""
    y_pos = 180
    for color in colors_list:
        if 200 <= x <= 230 and y_pos <= y <= y_pos + 30:
            return color
        y_pos += 35
    
    # Check custom color button (adjusted position for 8 colors instead of 7)
    if 200 <= x <= 230 and 455 <= y <= 485:
        return "custom"
    
    return None

def handle_custom_color_click(x, y, custom_r, custom_g, custom_b):
    """Handle clicks in custom color picker mode. Returns (new_r, new_g, new_b, action)"""
    # Red slider
    if 300 <= x <= 450 and 195 <= y <= 215:
        new_r = max(0, min(255, int((x - 300) / 150 * 255)))
        return (new_r, custom_g, custom_b, "adjust")
    
    # Green slider
    if 300 <= x <= 450 and 245 <= y <= 265:
        new_g = max(0, min(255, int((x - 300) / 150 * 255)))
        return (custom_r, new_g, custom_b, "adjust")
    
    # Blue slider
    if 300 <= x <= 450 and 295 <= y <= 315:
        new_b = max(0, min(255, int((x - 300) / 150 * 255)))
        return (custom_r, custom_g, new_b, "adjust")
    
    # Apply button
    if 200 <= x <= 280 and 420 <= y <= 450:
        return (custom_r, custom_g, custom_b, "apply")
    
    # Back button
    if 320 <= x <= 400 and 420 <= y <= 450:
        return (custom_r, custom_g, custom_b, "back")
    
    return (custom_r, custom_g, custom_b, None)

