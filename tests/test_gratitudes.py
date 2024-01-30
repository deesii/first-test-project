from lib.gratitudes import Gratitudes # Gratitudes brings in the class from lib


def test_gratitude_empty():
    gratitudes_instance = Gratitudes()
    gratitudes_instance.add("")
    result = gratitudes_instance.format()
    assert result == "Be grateful for: "


def test_add_gratitude():
    gratitudes_instance = Gratitudes()
    gratitudes_instance.add("humour")
    assert gratitudes_instance.gratitudes == ["humour"]
    

def test_add_gratitude_multiple():
    gratitudes_instance = Gratitudes()
    gratitudes_instance.add("humour")
    gratitudes_instance.add("life")
    assert gratitudes_instance.gratitudes == ["humour", "life"]


def test_format_gratitude():
    gratitude_instance = Gratitudes()
    format_output = gratitude_instance.format()
    assert format_output == "Be grateful for: "


def test_format_gratitude_multiple():
    gratitudes_instance = Gratitudes()
    gratitudes_instance.add("humour")
    gratitudes_instance.add("life")
    format_output = gratitudes_instance.format()
    assert format_output == "Be grateful for: humour, life"




# def test_add_gratitude():
#     gratitudes = Gratitudes()
