
waste_guidance = {

    "battery": {
        "category": "Hazardous / E-Waste",
        "guidance": (
            "Do not place batteries in regular household waste. "
            "Use an appropriate battery or e-waste collection facility."
        ),
        "tip": (
            "Proper battery disposal helps prevent harmful chemicals "
            "from entering soil and water."
        )
    },

    "biological": {
        "category": "Organic / Wet Waste",
        "guidance": (
            "Place biological waste in the appropriate organic "
            "or wet-waste stream."
        ),
        "tip": (
            "Organic waste can often be composted instead of "
            "being sent to landfill."
        )
    },

    "cardboard": {
        "category": "Recyclable / Dry Waste",
        "guidance": (
            "Keep cardboard clean and dry and place it in the "
            "appropriate recyclable collection stream."
        ),
        "tip": (
            "Recycling cardboard reduces the need for new "
            "raw materials."
        )
    },

    "glass": {
        "category": "Recyclable Waste",
        "guidance": (
            "Place clean glass containers in the appropriate "
            "glass/recyclable collection stream. Follow local "
            "rules for broken glass."
        ),
        "tip": (
            "Glass can be recycled repeatedly without losing "
            "its basic material properties."
        )
    },

    "metal": {
        "category": "Recyclable / Dry Waste",
        "guidance": (
            "Place clean metal containers or objects in the "
            "appropriate recyclable collection stream."
        ),
        "tip": (
            "Recycling metals saves energy and reduces the need "
            "for extracting new raw materials."
        )
    },

    "paper": {
        "category": "Recyclable / Dry Waste",
        "guidance": (
            "Keep paper reasonably clean and dry and place it "
            "in the appropriate recyclable collection stream."
        ),
        "tip": (
            "Recycling paper helps reduce pressure on forests "
            "and saves resources."
        )
    },

    "plastic": {
        "category": "Recyclable / Dry Waste",
        "guidance": (
            "Check whether the plastic item is accepted by your "
            "local recycling system before disposal."
        ),
        "tip": (
            "Reducing and reusing plastic is generally preferable "
            "to recycling alone."
        )
    },

    "clothes": {
        "category": "Textile / Reuse",
        "guidance": (
            "Consider donating, reusing, or sending usable textiles "
            "to an appropriate textile collection facility."
        ),
        "tip": (
            "Reusing clothing extends product life and reduces "
            "textile waste."
        )
    },

    "shoes": {
        "category": "Textile / Reuse",
        "guidance": (
            "Consider donating or reusing usable shoes, or use "
            "an appropriate textile/shoe collection program."
        ),
        "tip": (
            "Reuse keeps usable products out of the waste stream "
            "for longer."
        )
    },

    "trash": {
        "category": "Residual Waste",
        "guidance": (
            "Place the item in the appropriate residual-waste "
            "stream if it cannot be reused, recycled, composted, "
            "or safely recovered."
        ),
        "tip": (
            "Try to reduce, reuse, or recycle materials before "
            "sending them to residual waste."
        )
    }
}
def get_guidance(label):

    normalized_label = label.lower().strip()

    return waste_guidance.get(normalized_label)