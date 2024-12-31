import os
from crewai import Agent, Task, Crew
from typing import Dict, List
from dotenv import load_dotenv

load_dotenv()

# Define the job description
job_description = """
Título del Puesto: Gerente Senior de Producto - Asistente de Chat con IA

Acerca del Puesto:
Estamos buscando un Gerente de Producto innovador para liderar el desarrollo de un asistente de chat con IA de vanguardia que transformará la interacción y el compromiso de los usuarios. El candidato ideal impulsará la estrategia del producto, la experiencia del usuario y el desarrollo de funciones para una plataforma de IA conversacional inteligente.

Responsabilidades Clave:
- Definir la visión y la hoja de ruta del producto para un asistente de chat con IA
- Realizar investigaciones de usuarios para identificar características clave y casos de uso
- Colaborar con ingenieros de IA/ML para traducir las capacidades técnicas en funciones centradas en el usuario
- Diseñar y priorizar los requisitos del producto equilibrando la viabilidad técnica y las necesidades del usuario
- Desarrollar y realizar un seguimiento de los indicadores clave de rendimiento (KPIs) para la adopción, el compromiso y la satisfacción del usuario
- Trabajar de cerca con los equipos de diseño, ingeniería y ciencias de datos para mejorar el producto de forma iterativa
- Gestionar el ciclo de vida completo de desarrollo del producto

Requisitos Obligatorios:
- Más de 5 años de experiencia en gestión de productos, preferentemente en IA, SaaS o tecnologías conversacionales
- Sólida comprensión del desarrollo de productos de IA/ML
- Experiencia en definir estrategias de producto para software complejo e inteligente
- Excelentes habilidades de comunicación y colaboración multifuncional
- Historial comprobado de lanzamiento de productos digitales exitosos
- Profunda curiosidad por las tecnologías emergentes de IA

Habilidades Deseables:
- Antecedentes en procesamiento de lenguaje natural
- Experiencia con productos de IA generativa
- Conocimiento técnico de modelos de lenguaje de gran escala
"""


# List of resumes
resumes = [
    {
        "name": "Sarah Chen",
        "resume": (
            "Sarah Chen aprovechó su formación en ciencias de la computación para pasar "
            "a la gestión de productos en una startup de IA en rápido crecimiento. "
            "Lanzó con éxito tres productos de aprendizaje automático que aumentaron "
            "los ingresos de la empresa en un 40% en dos años. Su experiencia en la toma "
            "de decisiones basadas en datos y metodologías ágiles le permitió optimizar "
            "los procesos de desarrollo de productos. Sarah posee una maestría en Ciencias "
            "de la Computación de la Universidad de Stanford y cuenta con amplia experiencia "
            "en diseño de experiencia de usuario. Ha sido reconocida por su capacidad de "
            "conectar requisitos técnicos y comerciales en entornos tecnológicos de alto "
            "crecimiento."
        )
    },
    {
        "name": "Michael Rodriguez",
        "resume": (
            "Michael Rodriguez aporta 8 años de experiencia en gestión de productos de "
            "software empresarial gracias a su trayectoria en empresas tecnológicas de la "
            "lista Fortune 500. Tiene un historial comprobado de gestionar productos SaaS "
            "complejos que atienden a clientes empresariales de gran escala en múltiples "
            "industrias. El enfoque estratégico de Michael para el desarrollo de productos "
            "ha resultado constantemente en tasas de adopción de usuarios de dos dígitos y "
            "mejoras significativas en la satisfacción del cliente. Es experto en realizar "
            "investigaciones de mercado exhaustivas y traducir las percepciones de los "
            "clientes en hojas de ruta de producto accionables. Michael posee un MBA de la "
            "Universidad Northwestern con un enfoque en innovación tecnológica."
        )
    },
    {
        "name": "Elena Martinez",
        "resume": (
            "Elena Martinez se especializó en la gestión de productos de tecnología sanitaria, "
            "impulsando la transformación digital de plataformas de compromiso con los pacientes. "
            "Su profundo entendimiento de las regulaciones sanitarias y el diseño centrado en el "
            "usuario le permitió desarrollar aplicaciones móviles compatibles con HIPAA que mejoraron "
            "la comunicación con los pacientes. Elena ha gestionado equipos multifuncionales para "
            "entregar productos que integran sistemas de salud complejos y mejoran la eficiencia "
            "operativa. Aporta una combinación única de conocimientos técnicos y diseño basado en la "
            "empatía. Elena completó su certificación en Gestión de Productos en el programa de "
            "Educación Ejecutiva de UC Berkeley."
        )
    },
    {
        "name": "Jason Wang",
        "resume": (
            "Jason Wang ha pasado los últimos seis años liderando equipos de producto en plataformas "
            "de comercio electrónico de alto crecimiento, entregando constantemente funciones que "
            "generan ingresos. Su experiencia en optimización de la conversión y diseño de experiencia "
            "de usuario ha contribuido directamente a aumentar las ventas en línea en más del 60% en "
            "múltiples empresas. Jason es experto en el uso de análisis de datos para guiar las "
            "decisiones de producto y cuenta con amplia experiencia en pruebas A/B y análisis de "
            "comportamiento del usuario. Ha gestionado equipos de producto a nivel global y comprende "
            "las complejidades de crear experiencias digitales escalables y fáciles de usar. Jason "
            "tiene una licenciatura en Administración de Empresas con especialización menor en "
            "Ciencias de la Computación."
        )
    },
    {
        "name": "Aria Patel",
        "resume": (
            "Aria Patel aporta una combinación única de conocimientos financieros y habilidades de "
            "gestión de productos por su trabajo en startups fintech. Ha desarrollado soluciones de "
            "pago innovadoras y herramientas de seguimiento de inversiones que han sido adoptadas "
            "por más de 500.000 usuarios. La capacidad de Aria para comprender regulaciones "
            "financieras complejas y al mismo tiempo crear experiencias de usuario intuitivas la "
            "distingue en el campo de la gestión de productos. Tiene experiencia en gestionar el "
            "ciclo de vida completo de un producto y colaborar con equipos de ingeniería, diseño y "
            "marketing. Aria completó su Certificación Profesional en Gestión de Productos en MIT "
            "Professional Education."
        )
    },
    {
        "name": "Carlos Gomez",
        "resume": (
            "Carlos Gomez se ha especializado en la creación de productos para mercados emergentes, "
            "con amplia experiencia en los ecosistemas tecnológicos de América Latina y el sudeste "
            "asiático. Su enfoque de gestión de productos se centra en comprender las necesidades "
            "locales y crear soluciones que aborden desafíos específicos del mercado. Carlos ha "
            "lanzado aplicaciones móviles que han superado el millón de descargas en varios países "
            "en desarrollo. Es experto en realizar investigaciones de campo con los usuarios y "
            "adaptar estrategias de productos globales a contextos locales. Carlos posee un doble "
            "título en Negocios Internacionales e Innovación Digital."
        )
    },
    {
        "name": "Rebecca Liu",
        "resume": (
            "Rebecca Liu ha dedicado su carrera a transformar experiencias educativas mediante la "
            "gestión de productos tecnológicos. Ha desarrollado plataformas de aprendizaje adaptativo "
            "utilizadas por más de 100 distritos escolares, mejorando el compromiso de los estudiantes "
            "y los resultados de aprendizaje. La formación de Rebecca en psicología educativa le "
            "permite crear productos que realmente abordan los desafíos de aprendizaje. Tiene "
            "experiencia en gestionar relaciones con diversos interesados, incluidos educadores, "
            "administradores y equipos de tecnología. Rebecca completó su maestría en Tecnologías "
            "de Aprendizaje en Teachers College de la Universidad de Columbia."
        )
    },
    {
        "name": "Alex Rodriguez",
        "resume": (
            "Alex Rodriguez aporta una experiencia dinámica en gestión de productos desde el sector de "
            "videojuegos competitivos y tecnología del entretenimiento. Ha lanzado múltiples "
            "plataformas de juegos y experiencias digitales que alcanzaron a millones de usuarios en "
            "todo el mundo. Alex es experto en liderar equipos de desarrollo ágiles, realizar análisis "
            "de retroalimentación de jugadores y crear hojas de ruta de productos digitales "
            "atractivas. Su comprensión de las mecánicas de compromiso del usuario ha sido clave para "
            "desarrollar plataformas interactivas exitosas. Alex tiene una licenciatura en Diseño de "
            "Medios Interactivos."
        )
    },
    {
        "name": "Samira Khan",
        "resume": (
            "Samira Khan se centra en desarrollar productos tecnológicos que abordan desafíos "
            "críticos de sostenibilidad. Su experiencia en gestión de productos incluye la creación "
            "de soluciones de software para el seguimiento de energías renovables, la gestión de la "
            "huella de carbono y la optimización de la cadena de suministro sostenible. Samira tiene "
            "un enfoque holístico para el desarrollo de productos, considerando el impacto "
            "medioambiental junto con las métricas de negocio tradicionales. Ha gestionado equipos "
            "de producto a nivel internacional y ha lanzado productos con éxito en los mercados "
            "europeo y norteamericano. Samira completó su certificación en Estrategia Empresarial "
            "Sostenible en la Escuela de Negocios de Harvard."
        )
    },
    {
        "name": "Daniel Park",
        "resume": (
            "Daniel Park se especializa en gestión de productos para plataformas de inteligencia "
            "artificial y aprendizaje automático. Tiene amplia experiencia en traducir capacidades "
            "complejas de IA en productos fáciles de usar en diversas industrias, incluidas "
            "sanitaria, financiera y de atención al cliente. La formación técnica de Daniel en "
            "ciencias de la computación le permite comunicarse de manera efectiva entre los equipos "
            "de ingeniería y las partes interesadas del negocio. Ha gestionado el desarrollo de "
            "productos impulsados por IA que han mejorado significativamente la eficiencia "
            "operativa de clientes empresariales. Daniel posee un doctorado en Aprendizaje "
            "Automático de la Universidad Carnegie Mellon."
        )
    }
]

# Create Candidate Screening Agent
candidate_screener = Agent(
    role="Especialista Senior en Adquisición de Talento",
    goal="Identificar a los 3 mejores candidatos que mejor se ajusten a la descripción del puesto para un Gerente Senior de Producto en el desarrollo de un Asistente de Chat con IA",
    backstory="""Eres un especialista en adquisición de talento con amplia experiencia en reclutamiento tecnológico, 
    particularmente en roles de IA y gestión de productos. Tu agudeza para los detalles te permite alinear de manera 
    precisa los perfiles de los candidatos con los requisitos del puesto.""",
    verbose=True,
    llm="gpt-3.5-turbo",
)

# Create Screening Task
screening_task = Task(
    description=f"""Revisa cuidadosamente la descripción del puesto y el currículum de cada candidato:
    1. Analiza cómo la experiencia de cada candidato se alinea con los requisitos del puesto.
    2. Presta especial atención a:
       - Experiencia en la gestión de productos de IA/ML
       - Conocimientos técnicos en software complejo
       - Historial de lanzamientos exitosos de productos
    3. Clasifica a los candidatos y proporciona una justificación detallada para las 3 mejores selecciones.
    4. Explica por qué estos candidatos destacan para este puesto específico de Gerente de Producto de Asistente de Chat con IA.
    5. Toda tu respuesta y tu razonamiento deben estar en español

    Descripción del Puesto:
    {job_description}

    Candidate Resumes:
    {', '.join([f"{candidate['name']}: {candidate['resume']}" for candidate in resumes])}
    """,
    expected_output="",
    agent=candidate_screener
)

# Instantiate the Crew
crew = Crew(
    agents=[candidate_screener],
    tasks=[screening_task],
    verbose=False,
)

# Kickoff the task
result = crew.kickoff()

#print(result)