import os
import barcode
from barcode.writer import ImageWriter

def test_barcode_generation(tmp_path):
    # Test verisi ve çıktı yolu
    user_data = "123456789"
    output_path = tmp_path / "test_barcode"
    
    # Barkod oluşturma
    code = barcode.get('code128', user_data, writer=ImageWriter())
    filename = code.save(str(output_path))
    
    # Dosyanın gerçekten oluşup oluşmadığını kontrol et
    assert os.path.exists(filename)
    assert filename.endswith('.png')
