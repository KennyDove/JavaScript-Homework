{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "from datetime import datetime \n",
    "import os\n",
    "import time\n",
    "from urllib.parse import urlsplit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Defining path to open nasa site\n",
    "executable_path = {'executable_path':\"/usr/local/bin/chromedriver\"}\n",
    "brow = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# putting in the nasa site\n",
    "nasa = \"https://mars.nasa.gov/news\"\n",
    "brow.visit(nasa)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = brow.html\n",
    "soup = BeautifulSoup(html,\"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "News Title: Mars Now\n",
      "Paragraphs: The Red Planet's surface has been visited by eight NASA spacecraft. The ninth will be the first that includes a roundtrip ticket in its flight plan. \n"
     ]
    }
   ],
   "source": [
    "title = soup.find(\"div\", class_=\"content_title\").text\n",
    "paragraphs = soup.find(\"div\", class_=\"article_teaser_body\").text\n",
    "print(f\"News Title: {title}\")\n",
    "print(f\"Paragraphs: {paragraphs}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Finding images for Mars\n",
    "featured_image_url = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "brow.visit(featured_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.gov/\n"
     ]
    }
   ],
   "source": [
    "url = \"{0.scheme}://{0.netloc}/\".format(urlsplit(featured_image_url))\n",
    "print(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "//*[@id=\"page\"]/section[3]/div/ul/li[1]/a/div/div[2]/img\n"
     ]
    }
   ],
   "source": [
    "# path to get image\n",
    "xpath = \"//*[@id=\\\"page\\\"]/section[3]/div/ul/li[1]/a/div/div[2]/img\"\n",
    "print(xpath)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "results = brow.find_by_xpath(xpath)\n",
    "image = results[0]\n",
    "image.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# html_image = brow.html\n",
    "# img_url = soup.find(\"div\", class_=\"fancybox-image\")[\"src\"]\n",
    "# print(img_url)\n",
    "# Having a hard time pulling the data however using inspect we can find the url \n",
    "img_url = \"/spaceimages/images/largesize/PIA23948_hires.jpg\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.gov//spaceimages/images/largesize/PIA23948_hires.jpg\n"
     ]
    }
   ],
   "source": [
    "featured_imgurl = url + img_url \n",
    "print(featured_imgurl)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars Weather\n",
    "mars_weather_url = \"https://twitter.com/marswxreport?lang=en\"\n",
    "brow.visit(mars_weather_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "html_weather = brow.html\n",
    "soup2 = BeautifulSoup(html_weather, \"html.parser\")\n",
    "mars_weather = soup.find(\"p\", {\"class\": \"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text\"}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      0                              1\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       "5         Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                   -87 to -5 °C\n",
       "7         First Record:              2nd millennium BC\n",
       "8          Recorded By:           Egyptian astronomers"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Mars Facts and conversion from html to table\n",
    "mars_facts = \"https://space-facts.com/mars/\"\n",
    "table = pd.read_html(mars_facts)\n",
    "table[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Parameter</th>\n",
       "      <th>Values</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              Parameter                         Values\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       "5         Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                   -87 to -5 °C\n",
       "7         First Record:              2nd millennium BC\n",
       "8          Recorded By:           Egyptian astronomers"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# table clean up \n",
    "df_mars_facts = table[0]\n",
    "df_mars_facts.columns = [\"Parameter\", \"Values\"]\n",
    "df_mars_facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_facts_html_table = df_mars_facts.to_html()\n",
    "mars_facts_html_table = mars_facts_html_table.replace(\"\\n\",\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Hemispheres\n",
    "url_hemisphere = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "brow.visit(url_hemisphere)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://astrogeology.usgs.gov/\n"
     ]
    }
   ],
   "source": [
    "hemi_base_url = \"{0.scheme}://{0.netloc}/\".format(urlsplit(url_hemisphere))\n",
    "print(hemi_base_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cerberus Hemisphere Enhanced\n"
     ]
    }
   ],
   "source": [
    "# Cerberus Hemisphere\n",
    "hemisphere_imgurls = []\n",
    "# inspect the link and copy the xpath\n",
    "results = brow.find_by_xpath(\"//*[@id='product-section']/div[2]/div[1]/a/img\").click()\n",
    "cerberus_open_img = brow.find_by_xpath(\"//*[@id='wide-image']/img\").click()\n",
    "cerberus_img = brow.html\n",
    "soup = BeautifulSoup(cerberus_img, \"html.parser\")\n",
    "cerberus_url = soup.find(\"img\", class_=\"wide-image\")[\"src\"]\n",
    "cerberus_imgurl = hemi_base_url + cerberus_url\n",
    "cerberus_title = soup.find(\"h2\", class_=\"title\").text\n",
    "print(cerberus_title)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'image title': 'Cerberus Hemisphere Enhanced', 'image url': 'https://astrogeology.usgs.gov//cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'}\n"
     ]
    }
   ],
   "source": [
    "Cerberus = {\"image title\": cerberus_title, \"image url\": cerberus_imgurl}\n",
    "hemisphere_imgurls.append(Cerberus)\n",
    "print(Cerberus)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Return back to home page\n",
    "url_hemisphere = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "brow.visit(url_hemisphere)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'image title': 'Schiaparelli Hemisphere Enhanced', 'image url': 'https://astrogeology.usgs.gov//cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg'}\n"
     ]
    }
   ],
   "source": [
    "# Schiaparelli Hemisphere\n",
    "results2 = brow.find_by_xpath(\"//*[@id='product-section']/div[2]/div[2]/a/img\").click()\n",
    "open_schiaparelli = brow.find_by_xpath(\"//*[@id='wide-image']\").click()\n",
    "schiaparelli_img = brow.html\n",
    "soup = BeautifulSoup(schiaparelli_img, \"html.parser\")\n",
    "schiaparelli_url = soup.find(\"img\", class_=\"wide-image\")[\"src\"]\n",
    "schiaparelli_imgurl = hemi_base_url + schiaparelli_url\n",
    "schiaparelli_title = soup.find(\"h2\", class_=\"title\").text\n",
    "Schiaparelli = {\"image title\": schiaparelli_title, \"image url\": schiaparelli_imgurl}\n",
    "hemisphere_imgurls.append(Schiaparelli)\n",
    "print(Schiaparelli)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Return back to home page\n",
    "url_hemisphere = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "brow.visit(url_hemisphere)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Syrtis Major Hemisphere\n",
    "results3 = brow.find_by_xpath(\"//*[@id='product-section']/div[2]/div[3]/a/img\").click()\n",
    "syrtis_major_open = brow.find_by_xpath(\"//*[@id='wide-image']\").click()\n",
    "syrtis_major_img = brow.html\n",
    "soup = BeautifulSoup(syrtis_major_img, \"html.parser\")\n",
    "syrtis_major_url = soup.find(\"img\", class_=\"wide-image\")[\"src\"]\n",
    "syrtis_major_imgurl = hemi_base_url + syrtis_major_url\n",
    "syrtis_major_title = soup.find(\"h2\", class_=\"title\").text\n",
    "Syrtis_major = {\"image title\": syrtis_major_title, \"image url\": syrtis_major_imgurl}\n",
    "hemisphere_imgurls.append(Syrtis_major)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'image title': 'Syrtis Major Hemisphere Enhanced', 'image url': 'https://astrogeology.usgs.gov//cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg'}\n"
     ]
    }
   ],
   "source": [
    "print(Syrtis_major)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Return back to home page\n",
    "url_hemisphere = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "brow.visit(url_hemisphere)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Valles Marineris Hemisphere \n",
    "results4 = brow.find_by_xpath(\"//*[@id='product-section']/div[2]/div[4]/a/img\").click()\n",
    "marineris_open = brow.find_by_xpath(\"//*[@id='wide-image']\").click()\n",
    "marineris_image = brow.html\n",
    "soup = BeautifulSoup(marineris_image, \"html.parser\")\n",
    "marineris_url = soup.find(\"img\", class_=\"wide-image\")[\"src\"]\n",
    "marineris_imgurl = hemi_base_url + syrtis_major_url\n",
    "marineris_title = soup.find(\"h2\", class_=\"title\").text\n",
    "Valles_marineris = {\"image title\": marineris_title, \"image url\": marineris_imgurl}\n",
    "hemisphere_imgurls.append(Valles_marineris)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
