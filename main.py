import streamlit as st
from PIL import Image
import requests
import streamlit.components.v1 as components
import yfinance as yf
from datetime import date
from streamlit_player import st_player


class Tweet(object):
    def __init__(self, s, embed_str=False):
        if not embed_str:
            # Use Twitter's oEmbed API
            # https://dev.twitter.com/web/embedded-tweets
            api = "https://publish.twitter.com/oembed?url={}".format(s)
            response = requests.get(api)
            self.text = response.json()["html"]
        else:
            self.text = s

    def _repr_html_(self):
        return self.text

    def component(self, height):
        return components.html(self.text, height=height)


st.set_page_config(layout="wide")

row1_1, row1_2 = st.columns(2)

with row1_1:
    st.title('Críptomoneda en América Latina')
    st.subheader('Por William Yu')

with row1_2:
    st.markdown('###')
    st.write('''
    En 2008, una persona anónima, con el nombre *Satoshi Nakamoto*, hizo **Bitcoin**. Hoy, tiene valor más que un billón de dólares.
    Bitcoin, y otros críptomonedas, son herramientas únicas en América Latina, donde ciudadanos los usan para combatir la inflación.
    En los Estados Unidos, hay empresas (Square, Microstrategy, Coinbase, Tesla) que tienen inversiones en Bitcoin, pero por la mayoría 
    de la población, críptomoneda es solamente una apuesta. Pero, en América Latina, Bitcoin es cambiando las sístemas de banca, al nivel 
    de los gobiernos y leyes.
    ''')

st.markdown('##')

row2_1, row2_2 = st.columns(2)

with row2_1:
    st.subheader('**El Salvador**: El Gobierno contra La Población')
    st.write('''
    En los medios, especialmente de los Estados Unidos, los creyentes de Bitcoin y criptomonedas dicen que El Salvador es una victoria 
    muy importante. Pero, por los ciudadanos de El Salvador, ellos no sienten la emoción, pero miedo. Hay personas que creen sus presidente,
    Nayib Bukele, es un dictador, porque él no discutió sobre haciendo Bitcoin una moneda legal con los ciudadanos, las personas que hoy necesitan
    comprender esta tecnología. En el NFL, hay un ejemplo muy famoso en el mundo de Bitcoin de un jugador, Russell Okung, que recibió la mitad de su 
    salario en Bitcoin. Hoy, él es uno de los jugadores mejor pagados en el NFL. Este es muy diferente en la comparación de los ciudadanos de El Salvador,
    que tienen el miedo sobre teniendo que recibir sus salarios en Bitcoin porque las leyes. La mayoria de la población no tienen una garantía
    como un jugador en el NFL, entonces la sentimento es de miedo. 
    ''')
    st.write('''
    Bitcoin se supone que ayudar las personas pobres, que no tienen aceso de bancos, identificación, y que quieren anonimato. Pero, el presente es lejos de este
    sueño. El gobierno de El Salvador creyó y controla el app, Chivo, que la población necesita usar para participar en la vida nueva con Bitcoin. También, hoy, 
    Bitcoin está disfrutando meses de aumento, complementando la ley nueva de Bitcoin. Pero, ¿qué es lo que va a pasar cuando, no *si*, pero **cuando**, Bitcoin
    baja?
    ''')

with row2_2:
    img_elsalvador = Image.open('elsalvador.jpg')
    st.image(img_elsalvador)
    st.write('*Playa El Zonte, El Zonte, El Salvador*')


st.markdown('##')

st.subheader('El Precio de Bitcoin')

bitcoin = 'BTC-USD'
bitcoin_data = yf.Ticker(bitcoin)

today = date.today()

bitcoin_df = bitcoin_data.history(period='1d', start='2014-9-15', end=today)
st.line_chart(bitcoin_df.Close)

st.markdown('###')

row3_1, row3_2 = st.columns(2)

with row3_1:
    t = Tweet("https://twitter.com/nayibbukele/status/1449226485609504768?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Etweet").component(430)
    st.write('*Nayib Bukele, el Presidente de El Salvador*')

with row3_2:
    st.subheader('La Importancia de Remesas')

    st.write('''
    Remesas son el sistema donde una personas, usualmente un inmigrante, manda atrás dinero a su familia en su país de origen. Hoy, 20% de GDP de El Salvador 
    es por remesas, actualmente el sistema donde los bancos reciben todas de las cuotas, hasta 10%. Esta es la oportunidad grande con Bitcoin, porque usando
    el app Chivo, los ciudadanos pueden mandar y recibir remesas con cuotas menos que 1%, y el gobierno saca provecho. Aunque hay miedos sobre el impacto de 
    Bitcoin en vida diaria, por remesas, el sistema muy roto y amañando, hay finalmente cambio contra las cuotas de los bancos. 
    ''')
    st.write('''
    ¿Cómo Bitcoin relaciona con los bancos y la infraestructura tradicional? Actualmente, el Fondo Monetario Internacional es hablando con el gobierno de El
    Salvador sobre un $1.3 mil millones préstamo. El presidente del banco central de El Salvador, Douglas Rodriguez, dijo que Bitcoin no será visto un activo 
    arriesgado, pero un sistema legítimo. Él dice, "Nosotros no vemos algunos peligros." En el gobierno, personas son mandando el mensaje de inclusión financiera,
    especialmente en un país donde muchas ciudadanos no tienen aceso al internet.
    ''')

row4_1, row4_2 = st.columns(2)

with row4_1:
    st.subheader('Los Papeles de Las Figuras Americanas en Bitcoin')

    st.write('''
    Aunque Bitcoin tiene valor y un propósito en paises que tienen inflación, su papel en, por ejemplo, los Estados Unidos, es más borroso. Personas ven Bitcoin
    en maneras raras, confusas, y no relacionadas. Pero, hay figuras que están trabajando hacer Bitcoin una materia prima. 
    Jack Dorsey, CEO de Twitter y Square, cree que Bitcoin es el futuro del mundo, diciendo, "Bitcoin se unirá un país profundamente dividido." Hoy, usuarios de 
    Twitter pueden dar de propina a otros usarios usando Bitcoin, en un sistema muy similar al función de remesas. También, por su empresa de tecnología financiera,
    Square, Dorsey está trabajando tener Square hace tecnología minera por Bitcoin. En un país como los Estados Unidos, donde hay leyes por toda, este tiempo es 
    haciendo histora por cómo paises regula Bitcoin y otras críptomonedas. 
    ''')
    st.write('''
    El miedo común que Bitcoin es por criminales y el lavado de dinero es ***la barrera*** en los mentes de mucho de la población, en El Salvador, los Estados Unidos,
    y alguno país en el mundo. Pero, hay trabajo a parar estos miedos. En El Salvador, había personas revendiendo, o "scalping," Bitcoin en el app, Chivo. Fue ilegal, 
    porque Chivo congelaría el precio por los usuarios hacer un decisión imformados sobre comprando o vendiendo. El gobierno arregló el app para parar acciones ilegales. 
    En los Estados Unidos, corretajes, o "brokerages," donde personas pueden intercambiar críptomonedas, necesitan registrar con el gobierno - el sistema es cada vez más
    seguro.

    ''')

with row4_2:
    img_twitter = Image.open('twittertipjar.jpg')
    st.image(img_twitter)
    st.write('*Twitter "Tip Jar"*')
    
row5_1, row5_2 = st.columns(2)

with row5_1:
    img_ransomware = Image.open('ransomware.jpg')
    st.image(img_ransomware)

with row5_2:
    st.subheader('El Crimen con Críptomoneda')
    st.write('''
    Norteamérica es el blanco más grande del crimen usando críptomoneda en el mundo, hasta el punto donde norteamericanos dieron $131 millón al atacantes en
    el año pasado. El grupo de investigación, *Chainalysis*, siguió el dinero, y ellos creen que muchos de los atacantes son de Rusia. Por ejemplo, grupos
    de ransomware como NetWalker atacaron organizaciones, hospitales, y empresas en los Estados Unidos, exigiendo dinero en la forma de críptomoneda. Esta es 
    la forma nueva de guerra, usando tecnología y anonimato de críptomonedas a atacar. El presidente de los Estados Unidos, Joe Biden, exigió que el presidente 
    de Rusia, Vladimir Putin, a controlar estos grupos de ransomware, porque él lo va a terrorismo. 
    ''')
    st.write('''
    Aunque *Chainalysis* describe estos acciones ilegales, ellos dicen que ransomware y críptomoneda por crimen es raro. Este aspecto de críptomoneda es porque su
    naturaleza, donde transacciones son anónimos y por el internet. Pero, es hipócrito por bancos como JPMorgan o el Banco Central Europeo decir que bitcoin es por
    criminales, porque criminales usan la moneda fíat todos los días. 
    ''')

st.subheader('"El *Stablecoin*"')

usdc = 'USDC-USD'
usdc_data = yf.Ticker(usdc)

usdc_df = usdc_data.history(period='1d', start='2018-10-08', end=today)
st.line_chart(usdc_df.Close)

row6_1, row6_2 = st.columns(2)

with row6_1:
    st.subheader('Críptomoneda, Pero ¿Libre de Riesgos?')

    st.write('''
    *Valiu* es una empresa de carteras por críptomonedas, con muchos usuarios en Venezuela. El propósito de esta empresa es por los ciudadanos y sus necesidades.
    Un director, Tomas Fox, dijo, "So many Latin American countries have economic instability, so the people aren't really interested in trading cryptocurrency
    or getting exposure to Bitcoin because it's going to $80,000... People are trying to survive, so they need the ability to switch between their local currency
    and cryptocurrency to preserve its value." Este es donde el *stablecoin* tiene valor. Esta críptomoneda sigue el dolar de los Estados Unidos, entonces es como
    una mondea fíat. Pero, es todo digital. 
    ''')
    st.write('''
    *$USDC* es un ejemplo de un stablecoin, pero hay otros - Tether, Dao, GUSD, etc. Stablecoins resolven la problema más grande que muchas personas tienen con
    bitcoin o otras críptomonedas - el riesgo. Como el precio es siempre un dolar, críptomoneda se converten a su tecnología - *el blockchain*.
    ''')

with row6_2:
    img_usdc = Image.open('stablecoin.jpg')
    st.image(img_usdc)


row7_1, row7_2 = st.columns(2)

with row7_1:
    img_map = Image.open('map.jpg')
    st.image(img_map)


with row7_2:    
    st_player('https://www.youtube.com/watch?v=4_I2k8JYtF8')