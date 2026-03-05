from PyQt5.QtCore import QThread, pyqtSignal

class ScraperWorker(QThread):
    # Sinyal untuk berkomunikasi dengan main thread (GUI)
    article_ready = pyqtSignal(dict)
    progress_update = pyqtSignal(int, int)
    finished = pyqtSignal()
    error_occurred = pyqtSignal(str)
    
    def __init__(self, url, limit=0, start_date=None, end_date=None, parent=None):
        super(ScraperWorker, self).__init__(parent)
        self.url = url
        self.limit = limit
        self.start_date = start_date
        self.end_date = end_date
        self.is_running = True
    
    #method menjalankan thread
    def run(self):
        try:
            # Simulasi progress awal
            self.progress_update.emit(0, 100)
            
            # Simulasi progress
            if self.is_running:
                # Contoh pengiriman data artikel
                # self.article_ready.emit({"title": "Contoh Judul", "url": "http.../..."})
                
                self.progress_update.emit(100, 100)
                self.finished.emit()
                
        except Exception as e:
            self.error_occurred.emit(f"Terjadi kesalahan: {str(e)}")

    #method menghentikan scrapping
    def stop(self):
        self.is_running = False