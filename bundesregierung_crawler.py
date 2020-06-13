# python -m pip install icrawler
from icrawler.builtin import GoogleImageCrawler

#Bilder für alle Kabinettsmitglieder crawlen
#Das Verzeichnis muss an gepasst werden von "C:\Users\Nils\Desktop" auf Dich
google_crawler = GoogleImageCrawler(storage={"root_dir": r"C:\Users\Nils\Desktop\project_bundesregierung\bilder\Andreas Scheuer"})
google_crawler.crawl(keyword=" 'Andreas Scheuer'", max_num=10)

google_crawler = GoogleImageCrawler(storage={"root_dir": r"C:\Users\Nils\Desktop\project_bundesregierung\bilder\Angela Merkel"})
google_crawler.crawl(keyword=" 'Angela Merkel'", max_num=100)

google_crawler = GoogleImageCrawler(storage={"root_dir": r"C:\Users\Nils\Desktop\project_bundesregierung\bilder\Anja Karliczek"})
google_crawler.crawl(keyword=" 'Anja Karliczek'", max_num=100)

google_crawler = GoogleImageCrawler(storage={"root_dir": r"C:\Users\Nils\Desktop\project_bundesregierung\bilder\Annegret Kramp-Karrenbauer"})
google_crawler.crawl(keyword=" 'Annegret Kramp-Karrenbauer'", max_num=100)

google_crawler = GoogleImageCrawler(storage={"root_dir": r"C:\Users\Nils\Desktop\project_bundesregierung\bilder\Christine Lambrecht"})
google_crawler.crawl(keyword=" 'Christine Lambrecht'", max_num=100)

google_crawler = GoogleImageCrawler(storage={"root_dir": r"C:\Users\Nils\Desktop\project_bundesregierung\bilder\Franziska Giffey"})
google_crawler.crawl(keyword=" 'Franziska Giffey'", max_num=100)

google_crawler = GoogleImageCrawler(storage={"root_dir": r"C:\Users\Nils\Desktop\project_bundesregierung\bilder\Gerd Mueller"})
google_crawler.crawl(keyword=" 'Gerd Mueller BMZ'", max_num=100)

google_crawler = GoogleImageCrawler(storage={"root_dir": r"C:\Users\Nils\Desktop\project_bundesregierung\bilder\Heiko Maas"})
google_crawler.crawl(keyword=" 'Heiko Maas'", max_num=100)

google_crawler = GoogleImageCrawler(storage={"root_dir": r"C:\Users\Nils\Desktop\project_bundesregierung\bilder\Helge Braun"})
google_crawler.crawl(keyword=" 'Helge Braun'", max_num=100)

google_crawler = GoogleImageCrawler(storage={"root_dir": r"C:\Users\Nils\Desktop\project_bundesregierung\bilder\Horst Seehofer"})
google_crawler.crawl(keyword=" 'Horst Seehofer'", max_num=100)

google_crawler = GoogleImageCrawler(storage={"root_dir": r"C:\Users\Nils\Desktop\project_bundesregierung\bilder\Hubertus Heil"})
google_crawler.crawl(keyword=" 'Hubertus Heil'", max_num=100)

google_crawler = GoogleImageCrawler(storage={"root_dir": r"C:\Users\Nils\Desktop\project_bundesregierung\bilder\Julia Kloeckner"})
google_crawler.crawl(keyword=" 'Julia Kloeckner'", max_num=100)

google_crawler = GoogleImageCrawler(storage={"root_dir": r"C:\Users\Nils\Desktop\project_bundesregierung\bilder\Olaf Scholz"})
google_crawler.crawl(keyword=" 'Olaf Scholz'", max_num=100)

google_crawler = GoogleImageCrawler(storage={"root_dir": r"C:\Users\Nils\Desktop\project_bundesregierung\bilder\Jens Spahn"})
google_crawler.crawl(keyword=" 'Jens Spahn'", max_num=100)

google_crawler = GoogleImageCrawler(storage={"root_dir": r"C:\Users\Nils\Desktop\project_bundesregierung\bilder\Peter Altmeier"})
google_crawler.crawl(keyword=" 'Peter Altmeier'", max_num=100)

google_crawler = GoogleImageCrawler(storage={"root_dir": r"C:\Users\Nils\Desktop\project_bundesregierung\bilder\Svenja Schulze"})
google_crawler.crawl(keyword=" 'Svenja Schulze'", max_num=100)
