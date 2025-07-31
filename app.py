import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import os
from typing import List, Dict, Any


st.set_page_config(
    page_title="StudyCode - Plataforma de Estudos",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    .main {
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #f8f9ff 0%, #e8f4f8 50%, #f0f8ff 100%);
        background-attachment: fixed;
    }
    
.hero-section {
  position: relative;
  background-image: url('https://dkrn4sk0rn31v.cloudfront.net/uploads/2020/09/dicas-de-como-estudar-programacao.png');
  background-size: cover;
  background-position: center;
  height: 300px;
  border-radius: 20px;
  overflow: hidden;
  margin-bottom: 30px;
}

.overlay {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* escurece a imagem */
}

.hero-content {
  position: relative;
  z-index: 1;
  text-align: center;
  color: white;
  padding: 60px 20px;
}

.hero-title {
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 10px;
  text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7); /* sombra preta pro texto branco */
}

.hero-subtitle {
  font-size: 18px;
  text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7);
}



    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 20px;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
        animation: fadeInUp 1s ease-out;
        color: #34495e;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        font-weight: 300;
        opacity: 0.8;
        animation: fadeInUp 1s ease-out 0.3s both;
        color: #5a6c7d;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #a8e6cf, #88d8c0);
        padding: 25px;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 20px;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .metric-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(0,0,0,0.15);
    }
    
    .metric-card.blue {
        background: linear-gradient(135deg, #a8d8ea, #7fb3d3);
    }
    
    .metric-card.green {
        background: linear-gradient(135deg, #c7e9b4, #a1d99b);
    }
    
    .metric-card.purple {
        background: linear-gradient(135deg, #d4b5f7, #c19ee0);
    }
    
    .metric-card.orange {
        background: linear-gradient(135deg, #ffcc9c, #ffb07c);
    }
    
    .topic-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        border: 1px solid rgba(255,255,255,0.3);
        transition: all 0.3s ease;
    }
    
    .topic-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.12);
    }
    
    .difficulty-badge {
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
        margin: 5px;
    }
    
    .difficulty-iniciante {
        background: linear-gradient(135deg, #a8d8ea, #7fb3d3);
        color: white;
    }
    
    .difficulty-intermediario {
        background: linear-gradient(135deg, #ffcc9c, #ffb07c);
        color: white;
    }
    
    .difficulty-avancado {
        background: linear-gradient(135deg, #ffb3ba, #ff9aa2);
        color: white;
    }
    
    .session-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(248,250,252,0.9));
        backdrop-filter: blur(10px);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        border-left: 4px solid #a8d8ea;
        box-shadow: 0 3px 15px rgba(0,0,0,0.08);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .progress-container {
        background: rgba(255,255,255,0.95);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 30px;
        margin-bottom: 30px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        border: 1px solid rgba(255,255,255,0.3);
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,250,252,0.95));
        backdrop-filter: blur(10px);
    }
    
    .stSelectbox > div > div {
        background: rgba(255,255,255,0.95);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(200,200,200,0.3);
    }
    
    .stTextInput > div > div > input {
        background: rgba(255,255,255,0.95);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(200,200,200,0.3);
    }
    
    .stTextArea > div > div > textarea {
        background: rgba(255,255,255,0.95);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(200,200,200,0.3);
    }
    
    /* Estilo para botões do Streamlit */
    .stButton > button {
        background: linear-gradient(135deg, #a8d8ea, #7fb3d3);
        color: white;
        border: none;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #7fb3d3, #5a9bd4);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    /* Personalizar a sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, rgba(255,255,255,0.95), rgba(248,250,252,0.9));
    }
    
    /* Personalizar métricas do Streamlit */
    .metric-container {
        background: rgba(255,255,255,0.9);
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)


class StudyManager:
    def __init__(self):
        self.data_file = "study_data.json"
        self.load_data()
    
    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.topics = data.get('topics', [])
                self.sessions = data.get('sessions', [])
        else:
            self.topics = [
                {
                    "id": "1",
                    "title": "Python Avançado",
                    "description": "Decorators, generators, context managers e metaclasses",
                    "category": "Backend",
                    "difficulty": "Avançado",
                    "estimated_hours": 15,
                    "completed": False,
                    "resources": ["Real Python", "Python.org Documentation", "Effective Python"],
                    "created_at": "2024-01-15"
                },
                {
                    "id": "2",
                    "title": "Machine Learning com Scikit-learn",
                    "description": "Algoritmos de classificação, regressão e clustering",
                    "category": "Data Science",
                    "difficulty": "Intermediário",
                    "estimated_hours": 20,
                    "completed": True,
                    "resources": ["Scikit-learn Docs", "Hands-On ML", "Kaggle Learn"],
                    "created_at": "2024-01-10"
                },
                {
                    "id": "3",
                    "title": "FastAPI e APIs REST",
                    "description": "Criação de APIs modernas com FastAPI",
                    "category": "Backend",
                    "difficulty": "Intermediário",
                    "estimated_hours": 12,
                    "completed": False,
                    "resources": ["FastAPI Docs", "TestDriven.io", "YouTube Tutorials"],
                    "created_at": "2024-01-20"
                }
            ]
            self.sessions = [
                {
                    "id": "1",
                    "topic_id": "1",
                    "date": "2024-01-22",
                    "duration": 2.5,
                    "notes": "Estudei decorators e como criar meus próprios"
                },
                {
                    "id": "2",
                    "topic_id": "2",
                    "date": "2024-01-21",
                    "duration": 3.0,
                    "notes": "Implementei algoritmo de Random Forest"
                },
                {
                    "id": "3",
                    "topic_id": "3",
                    "date": "2024-01-23",
                    "duration": 1.5,
                    "notes": "Setup inicial do FastAPI e primeira rota"
                }
            ]
    
    def save_data(self):
        data = {
            'topics': self.topics,
            'sessions': self.sessions
        }
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def add_topic(self, topic_data):
        topic_data['id'] = str(len(self.topics) + 1)
        topic_data['created_at'] = datetime.now().strftime("%Y-%m-%d")
        topic_data['completed'] = False
        self.topics.append(topic_data)
        self.save_data()
    
    def add_session(self, session_data):
        session_data['id'] = str(len(self.sessions) + 1)
        session_data['date'] = datetime.now().strftime("%Y-%m-%d")
        self.sessions.append(session_data)
        self.save_data()
    
    def toggle_topic_completion(self, topic_id):
        for topic in self.topics:
            if topic['id'] == topic_id:
                topic['completed'] = not topic['completed']
                break
        self.save_data()
    
    def delete_topic(self, topic_id):
        self.topics = [t for t in self.topics if t['id'] != topic_id]
        self.sessions = [s for s in self.sessions if s['topic_id'] != topic_id]
        self.save_data()
    
    def get_stats(self):
        total_topics = len(self.topics)
        completed_topics = len([t for t in self.topics if t['completed']])
        total_hours = sum([s['duration'] for s in self.sessions])
        progress = (completed_topics / total_topics * 100) if total_topics > 0 else 0
        
        return {
            'total_topics': total_topics,
            'completed_topics': completed_topics,
            'total_hours': total_hours,
            'progress': progress
        }


if 'study_manager' not in st.session_state:
    st.session_state.study_manager = StudyManager()

study_manager = st.session_state.study_manager


st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">StudyCode</h1>
    <p class="hero-subtitle">.</p>
</div>
            
""", unsafe_allow_html=True)


st.sidebar.title("🎯 Navegação")
page = st.sidebar.selectbox(
    "Escolha uma seção:",
    ["📊 Dashboard", "📚 Tópicos de Estudo", "⏱️ Sessões de Estudo", "📈 Análises"]
)


if page == "📊 Dashboard":
    stats = study_manager.get_stats()
    
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card blue">
            <h2>📚</h2>
            <h3>{stats['total_topics']}</h3>
            <p>Total de Tópicos</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card green">
            <h2>✅</h2>
            <h3>{stats['completed_topics']}</h3>
            <p>Concluídos</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card purple">
            <h2>⏰</h2>
            <h3>{stats['total_hours']:.1f}h</h3>
            <p>Horas Estudadas</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card orange">
            <h2>🎯</h2>
            <h3>{stats['progress']:.1f}%</h3>
            <p>Progresso</p>
        </div>
        """, unsafe_allow_html=True)
    
  
    st.markdown("""
    <div class="progress-container">
        <h3>📈 Progresso Geral dos Estudos</h3>
    </div>
    """, unsafe_allow_html=True)
    
    progress_bar = st.progress(stats['progress'] / 100)
    st.write(f"**{stats['completed_topics']} de {stats['total_topics']} tópicos concluídos**")
    
   
    col1, col2 = st.columns(2)
    
    with col1:
        
        if study_manager.topics:
            categories = {}
            for topic in study_manager.topics:
                cat = topic['category']
                categories[cat] = categories.get(cat, 0) + 1
            
            fig_pie = px.pie(
                values=list(categories.values()),
                names=list(categories.keys()),
                title="📊 Tópicos por Categoria",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            fig_pie.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(255,255,255,0.9)',
                font=dict(family="Poppins")
            )
            st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        
        if study_manager.sessions:
            topic_hours = {}
            for session in study_manager.sessions:
                topic = next((t for t in study_manager.topics if t['id'] == session['topic_id']), None)
                if topic:
                    topic_name = topic['title']
                    topic_hours[topic_name] = topic_hours.get(topic_name, 0) + session['duration']
            
            fig_bar = px.bar(
                x=list(topic_hours.keys()),
                y=list(topic_hours.values()),
                title="⏱️ Horas Estudadas por Tópico",
                color=list(topic_hours.values()),
                color_continuous_scale="viridis"
            )
            fig_bar.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(255,255,255,0.9)',
                font=dict(family="Poppins"),
                xaxis_title="Tópicos",
                yaxis_title="Horas"
            )
            st.plotly_chart(fig_bar, use_container_width=True)


elif page == "📚 Tópicos de Estudo":
    st.title("📚 Gerenciar Tópicos de Estudo")
    
    
    with st.expander("➕ Adicionar Novo Tópico", expanded=False):
        with st.form("new_topic_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                title = st.text_input("📝 Título do Tópico")
                category = st.text_input("🏷️ Categoria", placeholder="Ex: Backend, Frontend, Data Science")
                difficulty = st.selectbox("⚡ Dificuldade", ["Iniciante", "Intermediário", "Avançado"])
            
            with col2:
                estimated_hours = st.number_input("⏰ Horas Estimadas", min_value=1, max_value=100, value=5)
                description = st.text_area("📄 Descrição", height=100)
                resources = st.text_area("📚 Recursos (um por linha)", height=100)
            
            if st.form_submit_button("✨ Criar Tópico", use_container_width=True):
                if title and category:
                    topic_data = {
                        'title': title,
                        'description': description,
                        'category': category,
                        'difficulty': difficulty,
                        'estimated_hours': estimated_hours,
                        'resources': [r.strip() for r in resources.split('\n') if r.strip()]
                    }
                    study_manager.add_topic(topic_data)
                    st.success("🎉 Tópico criado com sucesso!")
                    st.rerun()
                else:
                    st.error("❌ Preencha pelo menos o título e categoria!")
    
    
    st.subheader("📋 Seus Tópicos de Estudo")
    
    for topic in study_manager.topics:
        difficulty_class = f"difficulty-{topic['difficulty'].lower().replace('á', 'a').replace('é', 'e')}"
        
        st.markdown(f"""
        <div class="topic-card">
            <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 15px;">
                <div>
                    <h3 style="margin: 0; color: #2c3e50;">{'✅ ' if topic['completed'] else '📖 '}{topic['title']}</h3>
                    <span class="difficulty-badge {difficulty_class}">{topic['difficulty']}</span>
                    <span class="difficulty-badge" style="background: #3498db; color: white;">{topic['category']}</span>
                </div>
            </div>
            <p style="color: #7f8c8d; margin-bottom: 15px;">{topic['description']}</p>
            <div style="display: flex; gap: 20px; margin-bottom: 15px; font-size: 0.9rem; color: #7f8c8d;">
                <span>⏰ {topic['estimated_hours']}h estimadas</span>
                <span>📅 Criado em {topic['created_at']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        
        col1, col2, col3 = st.columns([1, 1, 4])
        
        with col1:
            if st.button("✅" if not topic['completed'] else "↩️", 
                        key=f"toggle_{topic['id']}", 
                        help="Marcar como concluído" if not topic['completed'] else "Marcar como não concluído"):
                study_manager.toggle_topic_completion(topic['id'])
                st.rerun()
        
        with col2:
            if st.button("🗑️", key=f"delete_{topic['id']}", help="Excluir tópico"):
                study_manager.delete_topic(topic['id'])
                st.rerun()
        
        
        if topic['resources']:
            with st.expander(f"📚 Recursos para {topic['title']}"):
                for resource in topic['resources']:
                    st.write(f"• {resource}")
        
        st.divider()


elif page == "⏱️ Sessões de Estudo":
    st.title("⏱️ Registrar Sessões de Estudo")
    
    
    with st.expander("➕ Registrar Nova Sessão", expanded=False):
        with st.form("new_session_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                topic_options = {topic['title']: topic['id'] for topic in study_manager.topics}
                selected_topic = st.selectbox("📚 Selecione o Tópico", list(topic_options.keys()))
                duration = st.number_input("⏰ Duração (horas)", min_value=0.5, max_value=12.0, value=1.0, step=0.5)
            
            with col2:
                notes = st.text_area("📝 Anotações da Sessão", height=150, 
                                   placeholder="O que você estudou? Quais conceitos aprendeu?")
            
            if st.form_submit_button("💾 Registrar Sessão", use_container_width=True):
                if selected_topic and notes:
                    session_data = {
                        'topic_id': topic_options[selected_topic],
                        'duration': duration,
                        'notes': notes
                    }
                    study_manager.add_session(session_data)
                    st.success("🎉 Sessão registrada com sucesso!")
                    st.rerun()
                else:
                    st.error("❌ Preencha todos os campos!")
    
   
    st.subheader("📋 Histórico de Sessões")
    
  
    sorted_sessions = sorted(study_manager.sessions, key=lambda x: x['date'], reverse=True)
    
    for session in sorted_sessions:
        topic = next((t for t in study_manager.topics if t['id'] == session['topic_id']), None)
        if topic:
            st.markdown(f"""
            <div class="session-card">
                <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 10px;">
                    <h4 style="margin: 0; color: #2c3e50;">📖 {topic['title']}</h4>
                    <div style="text-align: right; font-size: 0.9rem; color: #7f8c8d;">
                        <div>📅 {session['date']}</div>
                        <div>⏰ {session['duration']}h</div>
                    </div>
                </div>
                <p style="color: #34495e; margin: 0; font-style: italic;">"{session['notes']}"</p>
            </div>
            """, unsafe_allow_html=True)


elif page == "📈 Análises":
    st.title("📈 Análises Detalhadas")
    
    stats = study_manager.get_stats()
    
   
    if study_manager.sessions:
        
        df_sessions = pd.DataFrame(study_manager.sessions)
        df_sessions['date'] = pd.to_datetime(df_sessions['date'])
        df_sessions = df_sessions.sort_values('date')
        
       
        fig_timeline = px.line(
            df_sessions, 
            x='date', 
            y='duration',
            title='📊 Evolução das Horas de Estudo',
            markers=True,
            color_discrete_sequence=['#667eea']
        )
        fig_timeline.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(255,255,255,0.9)',
            font=dict(family="Poppins"),
            xaxis_title="Data",
            yaxis_title="Horas Estudadas"
        )
        st.plotly_chart(fig_timeline, use_container_width=True)
        
     
        difficulty_stats = {}
        for topic in study_manager.topics:
            diff = topic['difficulty']
            if diff not in difficulty_stats:
                difficulty_stats[diff] = {'total': 0, 'completed': 0, 'hours': 0}
            
            difficulty_stats[diff]['total'] += 1
            if topic['completed']:
                difficulty_stats[diff]['completed'] += 1
            
            
            topic_hours = sum([s['duration'] for s in study_manager.sessions if s['topic_id'] == topic['id']])
            difficulty_stats[diff]['hours'] += topic_hours
        
        
        difficulties = list(difficulty_stats.keys())
        total_topics = [difficulty_stats[d]['total'] for d in difficulties]
        completed_topics = [difficulty_stats[d]['completed'] for d in difficulties]
        hours_studied = [difficulty_stats[d]['hours'] for d in difficulties]
        
        fig_difficulty = go.Figure(data=[
            go.Bar(name='Total de Tópicos', x=difficulties, y=total_topics, marker_color='#3498db'),
            go.Bar(name='Tópicos Concluídos', x=difficulties, y=completed_topics, marker_color='#2ecc71'),
        ])
        
        fig_difficulty.update_layout(
            title='📊 Análise por Nível de Dificuldade',
            barmode='group',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(255,255,255,0.9)',
            font=dict(family="Poppins")
        )
        st.plotly_chart(fig_difficulty, use_container_width=True)
        
      
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🎯 Metas e Objetivos")
            
           
            avg_session_duration = sum([s['duration'] for s in study_manager.sessions]) / len(study_manager.sessions)
            
            st.metric("⏱️ Duração Média por Sessão", f"{avg_session_duration:.1f}h")
            st.metric("📅 Total de Sessões", len(study_manager.sessions))
            
            
            topic_hours = {}
            for session in study_manager.sessions:
                topic = next((t for t in study_manager.topics if t['id'] == session['topic_id']), None)
                if topic:
                    topic_name = topic['title']
                    topic_hours[topic_name] = topic_hours.get(topic_name, 0) + session['duration']
            
            if topic_hours:
                most_studied = max(topic_hours, key=topic_hours.get)
                st.metric("🏆 Tópico Mais Estudado", most_studied, f"{topic_hours[most_studied]:.1f}h")
        
        with col2:
            st.subheader("📊 Resumo por Categoria")
            
            category_stats = {}
            for topic in study_manager.topics:
                cat = topic['category']
                if cat not in category_stats:
                    category_stats[cat] = {'total': 0, 'completed': 0}
                
                category_stats[cat]['total'] += 1
                if topic['completed']:
                    category_stats[cat]['completed'] += 1
            
            for category, stats in category_stats.items():
                completion_rate = (stats['completed'] / stats['total']) * 100 if stats['total'] > 0 else 0
                st.write(f"**{category}**: {stats['completed']}/{stats['total']} ({completion_rate:.1f}%)")
                st.progress(completion_rate / 100)

# Footer
st.markdown("""
---
<div style="text-align: center; padding: 20px; color: black;">
    <p>🐍 <strong>StudyCode</strong> - Desenvolvido pelo Thiago Ferreira</p>
    <p>Organize seus estudos, acompanhe seu progresso e alcance seus objetivos!</p>
</div>
""", unsafe_allow_html=True)
