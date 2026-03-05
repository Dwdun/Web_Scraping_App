from PyQt5.QtCore import QThread, pyqtSignal

class ScraperWorker(QThread):
    # Sinyal untuk berkomunikasi dengan main thread (GUI)
    progress_updated = pyqtSignal(int)
    log_updated = pyqtSignal(str)
    finished_data = pyqtSignal(list)
    error_occurred = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super(ScraperWorker, self).__init__(parent)
        self.is_running = True
    
    #method menjalankan thread
    def run(self):
        try:
            self.log_updated.emit("Memulai proses scraping...")
            self.progress_updated.emit(10)
            
            # Simulasi progress
            if self.is_running:
                self.progress_updated.emit(100)
                self.log_updated.emit("Scraping selesai.")
                self.finished_data.emit([]) # Kirimkan list data hasil scraping
                
        except Exception as e:
            self.error_occurred.emit(f"Terjadi kesalahan: {str(e)}")

    #method menghentikan scrapping
    def stop(self):
        self.is_running = False
        self.log_updated.emit("Proses scraping dihentikan.")