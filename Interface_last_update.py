import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import numpy as np
from PIL import Image, ImageTk
from tkinter import font as tkFont


class ModernGraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graphes Aléatoires et Algorithmes")
        self.root.geometry("1000x800")
        self.root.configure(bg="#f7f9fc")

        # Variables for page management
        self.current_frame = None
        self.current_figure_canvas = None  # To store the current graph canvas

        # Create frames for each page
        self.home_frame = tk.Frame(root, bg="#f7f9fc")
        self.algorithms_frame = tk.Frame(root, bg="#f7f9fc")

        # Initialize components
        self.init_variables()
        self.create_home_page()
        self.create_algorithms_page()

        # Show the home page on startup
        self.show_home_page()

    def init_variables(self):
        # User variables
        self.n = tk.IntVar()
        self.p_min = tk.DoubleVar()
        self.p_max = tk.DoubleVar()
        self.num_vertices_mst = tk.IntVar()
        self.num_vertices_dijkstra = tk.IntVar()
        self.start_node = tk.StringVar()
        self.end_node = tk.StringVar()
        self.num_vertices_ford_fulkerson = tk.IntVar()
        self.source_node = tk.StringVar()
        self.sink_node = tk.StringVar()
        self.num_suppliers = tk.IntVar()
        self.num_consumers = tk.IntVar()
        self.cost_matrix = []
        self.num_vertices_bellman_ford = tk.IntVar()  # New variable for Bellman-Ford
        self.start_node_bellman_ford = tk.StringVar()  # New variable for Bellma
    def create_home_page(self):
        """Create the home page with a modern and creative design."""
        # Gradient background
        gradient_frame = tk.Frame(self.home_frame, bg="#ffffff")
        gradient_frame.pack(fill=tk.BOTH, expand=True)

        # Add an image or icon (replace with your image path)
        try:
            original_image = Image.open(r"C:\Users\issam\OneDrive\Bureau\RO\image.png")  # Use raw string
            resized_image = original_image.resize((600, 250))  # Resize the image
            self.logo_image = ImageTk.PhotoImage(resized_image)
            logo_label = tk.Label(gradient_frame, image=self.logo_image, bg="#ffffff")
            logo_label.pack(pady=(0, 30))
        except Exception as e:
            print(f"Error loading image: {e}")

        # Add a modern title with custom font
        title_font = tkFont.Font(family="Helvetica", size=28, weight="bold")
        subtitle_font = tkFont.Font(family="Helvetica", size=18, weight="bold")

        title = tk.Label(
            gradient_frame,
            text="Bienvenue dans l'Interface Graphique",
            font=title_font,
            bg="#ffffff",
            fg="#333",
        )
        title.pack(pady=(50, 10))

        subtitle = tk.Label(
            gradient_frame,
            text="Encadré par: Dr. EL MKHALET MOUNA",
            font=subtitle_font,
            bg="#ffffff",
            fg="#555",
        )
        subtitle.pack(pady=(0, 5))

        subtitle2 = tk.Label(
            gradient_frame,
            text="Réalisé par: LAMRHILI Issam",
            font=subtitle_font,
            bg="#ffffff",
            fg="#555",
        )
        subtitle2.pack(pady=(0, 30))

        # Continue button with hover effect
        continue_btn = tk.Button(
            gradient_frame,
            text="Continuer",
            command=self.show_algorithms_page,
            font=("Arial", 14),
            bg="#008000",
            fg="white",
            relief=tk.FLAT,
            width=20,
            height=2,
            bd=0,
            activebackground="#0f4d0f",
        )
        continue_btn.pack(pady=(10, 10))

        # Hover effect for Continue button
        def on_continue_hover(event):
            continue_btn.config(bg="#0f4d0f")  # Darker color on hover

        def on_continue_leave(event):
            continue_btn.config(bg="#008000")  # Original color

        continue_btn.bind("<Enter>", on_continue_hover)
        continue_btn.bind("<Leave>", on_continue_leave)

        # Quit button with hover effect
        quit_btn = tk.Button(
            gradient_frame,
            text="Quitter",
            command=self.quit_application,
            font=("Arial", 14),
            bg="#cd1c18",
            fg="white",
            relief=tk.FLAT,
            width=20,
            height=2,
            bd=0,
            activebackground="#cc0000",
        )
        quit_btn.pack(pady=(10, 50))

        # Hover effect for Quit button
        def on_quit_hover(event):
            quit_btn.config(bg="#ff6666")  # Darker color on hover

        def on_quit_leave(event):
            quit_btn.config(bg="#cc0000")  # Original color

        quit_btn.bind("<Enter>", on_quit_hover)
        quit_btn.bind("<Leave>", on_quit_leave)

        # Add a footer with a creative touch
        footer = tk.Label(
            gradient_frame,
            text="© 2025 - Tous droits réservés",
            font=("Arial", 10),
            bg="#ffffff",
            fg="#777",
        )
        footer.pack(side=tk.BOTTOM, pady=10)

    def create_algorithms_page(self):
        """Create the algorithms page with buttons for each algorithm."""
        # Back button to return to home
        back_btn = tk.Button(
            self.algorithms_frame,
            text="Retour à l'accueil",
            command=self.show_home_page,
            font=("Arial", 12),
            bg="#cd1c18",
            fg="white",
            relief=tk.FLAT
        )
        back_btn.pack(pady=10)

        # Frame to hold algorithm buttons
        button_frame = tk.Frame(self.algorithms_frame, bg="#ffffff")
        button_frame.pack(pady=20)

        # Buttons for each algorithm
        algorithms = [
            ("Welsh-Powell", self.show_welsh_powell_frame),
            ("Kruskal MST", self.show_kruskal_frame),
            ("Dijkstra", self.show_dijkstra_frame),
            ("Ford-Fulkerson", self.show_ford_fulkerson_frame),
            ("Potentiel-Métra", self.show_potentiel_metra_frame),
            ("Problème Transport", self.show_transport_problem_frame),
            
        ]

        for algo_name, algo_command in algorithms:
            btn = tk.Button(
                button_frame,
                text=algo_name,
                command=algo_command,
                font=("Arial", 12),
                bg="#008000",
                fg="white",
                relief=tk.FLAT,
                width=20,
            )
            btn.pack(pady=5)

        # Create frames for each algorithm
        self.welsh_powell_frame = tk.Frame(self.algorithms_frame, bg="#f7f9fc")
        self.create_welsh_powell_section(self.welsh_powell_frame)

        self.kruskal_frame = tk.Frame(self.algorithms_frame, bg="#f7f9fc")
        self.create_kruskal_section(self.kruskal_frame)

        self.dijkstra_frame = tk.Frame(self.algorithms_frame, bg="#f7f9fc")
        self.create_dijkstra_section(self.dijkstra_frame)

        self.ford_fulkerson_frame = tk.Frame(self.algorithms_frame, bg="#f7f9fc")
        self.create_ford_fulkerson_section(self.ford_fulkerson_frame)

        self.potentiel_metra_frame = tk.Frame(self.algorithms_frame, bg="#f7f9fc")
        self.create_potentiel_metra_section(self.potentiel_metra_frame)

        self.transport_problem_frame = tk.Frame(self.algorithms_frame, bg="#f7f9fc")
        self.create_transport_problem_section(self.transport_problem_frame)
        
        
        
    def show_home_page(self):
        """Show the home page and clear any displayed graph."""
        self.clear_graph()  # Clear the graph before switching to the home page
        if self.current_frame:
            self.current_frame.pack_forget()  # Hide the current frame
        self.home_frame.pack(fill=tk.BOTH, expand=True)  # Show the home frame
        self.current_frame = self.home_frame

    def show_algorithms_page(self):
        """Show the algorithms page."""
        self.clear_graph()  # Clear the graph before switching to the algorithms page
        if self.current_frame:
            self.current_frame.pack_forget()  # Hide the current frame
        self.algorithms_frame.pack(fill=tk.BOTH, expand=True)  # Show the algorithms frame
        self.current_frame = self.algorithms_frame

    def quit_application(self):
        """Quit the application."""
        self.root.quit()

    def clear_graph(self):
        """Clear the currently displayed graph."""
        if self.current_figure_canvas:
            self.current_figure_canvas.get_tk_widget().destroy()  # Destroy the graph canvas
            self.current_figure_canvas = None  # Reset the reference

    def show_welsh_powell_frame(self):
        """Show the Welsh-Powell frame."""
        self.hide_all_frames()
        self.welsh_powell_frame.pack(fill=tk.BOTH, expand=True)

    def show_kruskal_frame(self):
        """Show the Kruskal frame."""
        self.hide_all_frames()
        self.kruskal_frame.pack(fill=tk.BOTH, expand=True)

    def show_dijkstra_frame(self):
        """Show the Dijkstra frame."""
        self.hide_all_frames()
        self.dijkstra_frame.pack(fill=tk.BOTH, expand=True)

    def show_ford_fulkerson_frame(self):
        """Show the Ford-Fulkerson frame."""
        self.hide_all_frames()
        self.ford_fulkerson_frame.pack(fill=tk.BOTH, expand=True)

    def show_potentiel_metra_frame(self):
        """Show the Potentiel-Métra frame."""
        self.hide_all_frames()
        self.potentiel_metra_frame.pack(fill=tk.BOTH, expand=True)

    def show_moindre_cout_frame(self):
        """Show the Moindre Coût frame."""
        self.hide_all_frames()
        self.moindre_cout_frame.pack(fill=tk.BOTH, expand=True)

    def show_nord_ouest_frame(self):
        """Show the Nord-Ouest frame."""
        self.hide_all_frames()
        self.nord_ouest_frame.pack(fill=tk.BOTH, expand=True)

    def show_stepping_stone_frame(self):
        """Show the Stepping Stone frame."""
        self.hide_all_frames()
        self.stepping_stone_frame.pack(fill=tk.BOTH, expand=True)
        
    

    def hide_all_frames(self):
        """Hide all algorithm frames."""
        for frame in [
            self.welsh_powell_frame,
            self.kruskal_frame,
            self.dijkstra_frame,
            self.ford_fulkerson_frame,
            self.potentiel_metra_frame,
            self.transport_problem_frame,
            
        ]:
            frame.pack_forget()

    def create_welsh_powell_section(self, frame):
        """Create the Welsh-Powell section."""
        tk.Label(frame, text="Nombre de Sommets :", bg="#ffffff", font=("Arial", 12)).grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )
        tk.Entry(frame, textvariable=self.n, font=("Arial", 12)).grid(
            row=0, column=1, padx=5, pady=5
        )

        tk.Label(frame, text="Probabilité Min (0-1) :", bg="#ffffff", font=("Arial", 12)).grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        tk.Entry(frame, textvariable=self.p_min, font=("Arial", 12)).grid(
            row=1, column=1, padx=5, pady=5
        )

        tk.Label(frame, text="Probabilité Max (0-1) :", bg="#ffffff", font=("Arial", 12)).grid(
            row=2, column=0, padx=5, pady=5, sticky="w"
        )
        tk.Entry(frame, textvariable=self.p_max, font=("Arial", 12)).grid(
            row=2, column=1, padx=5, pady=5
        )

        tk.Button(
            frame,
            text="Générer le Graphe",
            command=self.generate_and_color_graph,
            font=("Arial", 12),
            bg="#008000",
            fg="white",
            relief=tk.FLAT,
        ).grid(row=3, column=0, columnspan=2, pady=10)

        tk.Button(
            frame,
            text="Supprimer le Graphe",
            command=self.clear_graph,
            font=("Arial", 12),
            bg="#cc0000",
            fg="white",
            relief=tk.FLAT,
        ).grid(row=4, column=0, columnspan=2, pady=10)

    def create_kruskal_section(self, frame):
        """Create the Kruskal MST section."""
        tk.Label(frame, text="Nombre de Sommets :", bg="#ffffff", font=("Arial", 12)).grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )
        tk.Entry(frame, textvariable=self.num_vertices_mst, font=("Arial", 12)).grid(
            row=0, column=1, padx=5, pady=5
        )

        tk.Button(
            frame,
            text="Générer et Appliquer Kruskal",
            command=self.generate_and_apply_kruskal,
            font=("Arial", 12),
            bg="#008000",
            fg="white",
            relief=tk.FLAT,
        ).grid(row=1, column=0, columnspan=2, pady=10)

        tk.Button(
            frame,
            text="Supprimer le Graphe",
            command=self.clear_graph,
            font=("Arial", 12),
            bg="#cc0000",
            fg="white",
            relief=tk.FLAT,
        ).grid(row=2, column=0, columnspan=2, pady=10)

    def create_dijkstra_section(self, frame):
        """Create the Dijkstra section."""
        tk.Label(frame, text="Nombre de Sommets :", bg="#ffffff", font=("Arial", 12)).grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )
        tk.Entry(frame, textvariable=self.num_vertices_dijkstra, font=("Arial", 12)).grid(
            row=0, column=1, padx=5, pady=5
        )

        tk.Label(frame, text="Noeud de Départ :", bg="#ffffff", font=("Arial", 12)).grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        tk.Entry(frame, textvariable=self.start_node, font=("Arial", 12)).grid(
            row=1, column=1, padx=5, pady=5
        )

        tk.Label(frame, text="Noeud d'Arrivée :", bg="#ffffff", font=("Arial", 12)).grid(
            row=2, column=0, padx=5, pady=5, sticky="w"
        )
        tk.Entry(frame, textvariable=self.end_node, font=("Arial", 12)).grid(
            row=2, column=1, padx=5, pady=5
        )

        tk.Button(
            frame,
            text="Générer et Appliquer Dijkstra",
            command=self.generate_and_apply_dijkstra,
            font=("Arial", 12),
            bg="#008000",
            fg="white",
            relief=tk.FLAT,
        ).grid(row=3, column=0, columnspan=2, pady=10)

        tk.Button(
            frame,
            text="Supprimer le Graphe",
            command=self.clear_graph,
            font=("Arial", 12),
            bg="#cc0000",
            fg="white",
            relief=tk.FLAT,
        ).grid(row=4, column=0, columnspan=2, pady=10)

    def create_ford_fulkerson_section(self, frame):
        """Create the Ford-Fulkerson section."""
        tk.Label(frame, text="Nombre de Sommets :", bg="#ffffff", font=("Arial", 12)).grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )
        tk.Entry(frame, textvariable=self.num_vertices_ford_fulkerson, font=("Arial", 12)).grid(
            row=0, column=1, padx=5, pady=5
        )

        tk.Label(frame, text="Noeud Source :", bg="#ffffff", font=("Arial", 12)).grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        tk.Entry(frame, textvariable=self.source_node, font=("Arial", 12)).grid(
            row=1, column=1, padx=5, pady=5
        )

        tk.Label(frame, text="Noeud Puit :", bg="#ffffff", font=("Arial", 12)).grid(
            row=2, column=0, padx=5, pady=5, sticky="w"
        )
        tk.Entry(frame, textvariable=self.sink_node, font=("Arial", 12)).grid(
            row=2, column=1, padx=5, pady=5
        )

        tk.Button(
            frame,
            text="Générer et Appliquer Ford-Fulkerson",
            command=self.generate_and_apply_ford_fulkerson,
            font=("Arial", 12),
            bg="#008000",
            fg="white",
            relief=tk.FLAT,
        ).grid(row=3, column=0, columnspan=2, pady=10)

        tk.Button(
            frame,
            text="Supprimer le Graphe",
            command=self.clear_graph,
            font=("Arial", 12),
            bg="#cc0000",
            fg="white",
            relief=tk.FLAT,
        ).grid(row=4, column=0, columnspan=2, pady=10)

    def create_potentiel_metra_section(self, frame):
        """Create the Potentiel-Métra section with a more organized layout."""
        # Create main container frame
        main_frame = tk.Frame(frame, bg="#f7f9fc")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
        # Input Section
        input_frame = tk.Frame(main_frame, bg="#f7f9fc")
        input_frame.pack(fill=tk.X, pady=(0, 20))
    
        # Number of tasks input
        tk.Label(
            input_frame,
            text="Nombre de Tâches :",
            bg="#f7f9fc",
            font=("Arial", 12, "bold")
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        task_entry = tk.Entry(
            input_frame,
            textvariable=self.n,
            font=("Arial", 12),
            width=10
        )
        task_entry.pack(side=tk.LEFT)
    
        # Buttons Section
        button_frame = tk.Frame(main_frame, bg="#f7f9fc")
        button_frame.pack(fill=tk.X, pady=(0, 20))
    
        # Generate button
        generate_btn = tk.Button(
            button_frame,
            text="Générer et Appliquer Potentiel-Métra",
            command=self.generate_and_apply_potentiel_metra,
            font=("Arial", 12),
            bg="#008000",
            fg="white",
            relief=tk.FLAT,
            width=30
        )
        generate_btn.pack(side=tk.LEFT, padx=(0, 10))
    
        # Delete button
        delete_btn = tk.Button(
            button_frame,
            text="Supprimer le Graphe",
            command=self.clear_potentiel_metra,
            font=("Arial", 12),
            bg="#cc0000",
            fg="white",
            relief=tk.FLAT,
            width=20
        )
        delete_btn.pack(side=tk.LEFT)
        
    
        # Create frames for results
        self.pm_table_frame = tk.Frame(main_frame, bg="#f7f9fc")
        self.pm_table_frame.pack(fill=tk.BOTH, expand=True)
    
        self.pm_graph_frame = tk.Frame(main_frame, bg="#f7f9fc")
        self.pm_graph_frame.pack(fill=tk.BOTH, expand=True)
        
        

    def clear_potentiel_metra(self):
        """Clear the Potentiel-Métra graph and table."""
        # Clear the table
        for widget in self.pm_table_frame.winfo_children():
            widget.destroy()
        
        # Clear the graph
        for widget in self.pm_graph_frame.winfo_children():
            widget.destroy()
        
        # Clear any matplotlib figure if it exists
        if self.current_figure_canvas:
            self.current_figure_canvas.get_tk_widget().destroy()
            self.current_figure_canvas = None
        
    
    def create_transport_problem_section(self, frame):
        """Create the unified transport problem section with all three methods."""
        # Input frame
        input_frame = tk.Frame(frame, bg="#f7f9fc")
        input_frame.pack(pady=10, fill=tk.X)
    
        # Supplier and Consumer inputs
        tk.Label(input_frame, text="Nombre de Fournisseurs :", bg="#ffffff", font=("Arial", 12)).grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )
        tk.Entry(input_frame, textvariable=self.num_suppliers, font=("Arial", 12)).grid(
            row=0, column=1, padx=5, pady=5
        )
    
        tk.Label(input_frame, text="Nombre de Consommateurs :", bg="#ffffff", font=("Arial", 12)).grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        tk.Entry(input_frame, textvariable=self.num_consumers, font=("Arial", 12)).grid(
            row=1, column=1, padx=5, pady=5
        )
    
        # Button frame
        button_frame = tk.Frame(frame, bg="#f7f9fc")
        button_frame.pack(pady=10)
        
       
    
        # Buttons for each method
        methods = [
            ("Méthode du Nord-Ouest", self.apply_nord_ouest),
            ("Méthode du Moindre Coût", self.apply_moindre_cout),
            ("Méthode de Stepping Stone", self.apply_stepping_stone)
        ]
    
        for text, command in methods:
            tk.Button(
                button_frame,
                text=text,
                command=command,
                font=("Arial", 12),
                bg="#008000",
                fg="white",
                relief=tk.FLAT,
                width=25
            ).pack(pady=5)
           # Add a "Supprimer le Tableau" button
        tk.Button(
            button_frame,
            text="Supprimer le Tableau",
            command=self.clear_transport_table,
            font=("Arial", 12),
            bg="#cc0000",
            fg="white",
            relief=tk.FLAT,
            width=25
        ).pack(pady=5)
    
        # Table frame
        self.table_frame = tk.Frame(frame, bg="#f7f9fc")
        self.table_frame.pack(pady=10, expand=True, fill=tk.BOTH)
        
    def clear_transport_table(self):
        """Clear the transport problem table."""
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        
        

    def generate_and_color_graph(self):
        """Generate a random graph and color it."""
        self.clear_graph()  # Clear the previous graph
        num_vertices = self.n.get()
        p_min = self.p_min.get()
        p_max = self.p_max.get()

        if p_min < 0 or p_max > 1 or p_min > p_max:
            messagebox.showerror("Erreur", "Veuillez entrer des probabilités valides (0 <= min <= max <= 1).")
            return

        # Generate a random graph
        prob = random.uniform(p_min, p_max)
        graph = nx.erdos_renyi_graph(num_vertices, prob)

        # Apply the Welsh-Powell algorithm for coloring
        colors = nx.coloring.greedy_color(graph, strategy="largest_first")

        # Display the graph
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(graph)
        nx.draw(
            graph,
            pos,
            with_labels=True,
            node_color=[colors[node] for node in graph.nodes()],
            node_size=500,
            cmap=plt.cm.tab20,
            font_weight="bold",
        )
        plt.title("Graphe généré et coloré avec Welsh-Powell")

        # Embed the matplotlib figure in Tkinter
        self.current_figure_canvas = FigureCanvasTkAgg(plt.gcf(), self.root)
        self.current_figure_canvas.get_tk_widget().pack(pady=10)
        plt.close()

    def generate_and_apply_kruskal(self):
        """Generate a random graph and apply Kruskal's algorithm."""
        self.clear_graph()  # Clear the previous graph
        num_vertices = self.num_vertices_mst.get()

        # Generate a random weighted graph
        graph = nx.complete_graph(num_vertices)
        for u, v in graph.edges():
            graph[u][v]['weight'] = random.randint(1, 10)

        # Apply Kruskal's algorithm
        mst = nx.minimum_spanning_tree(graph, algorithm='kruskal')

        # Display the graph
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(graph)
        nx.draw(
            graph,
            pos,
            with_labels=True,
            node_size=500,
            font_weight="bold",
        )
        nx.draw_networkx_edges(
            mst,
            pos,
            edge_color='r',
            width=2,
        )
        plt.title("Graphe généré et Arbre Couvrant Minimum (Kruskal)")

        # Embed the matplotlib figure in Tkinter
        self.current_figure_canvas = FigureCanvasTkAgg(plt.gcf(), self.root)
        self.current_figure_canvas.get_tk_widget().pack(pady=10)
        plt.close()

    def generate_and_apply_dijkstra(self):
        """Generate a random graph and apply Dijkstra's algorithm."""
        self.clear_graph()  # Clear the previous graph
        num_vertices = self.num_vertices_dijkstra.get()
        start_node = self.start_node.get()
        end_node = self.end_node.get()

        # Generate a random weighted graph
        graph = nx.complete_graph(num_vertices)
        for u, v in graph.edges():
            graph[u][v]['weight'] = random.randint(1, 10)

        # Apply Dijkstra's algorithm
        try:
            path = nx.dijkstra_path(graph, source=int(start_node), target=int(end_node))
            path_edges = list(zip(path, path[1:]))
        except nx.NetworkXNoPath:
            messagebox.showerror("Erreur", "Aucun chemin trouvé entre les noeuds spécifiés.")
            return

        # Display the graph
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(graph)
        nx.draw(
            graph,
            pos,
            with_labels=True,
            node_size=500,
            font_weight="bold",
        )
        nx.draw_networkx_edges(
            graph,
            pos,
            edgelist=path_edges,
            edge_color='r',
            width=2,
        )
        plt.title(f"Chemin le plus court (Dijkstra) de {start_node} à {end_node}")

        # Embed the matplotlib figure in Tkinter
        self.current_figure_canvas = FigureCanvasTkAgg(plt.gcf(), self.root)
        self.current_figure_canvas.get_tk_widget().pack(pady=10)
        plt.close()

    def generate_and_apply_ford_fulkerson(self):
        """Generate a random graph and apply the Ford-Fulkerson algorithm."""
        self.clear_graph()  # Clear the previous graph
        num_vertices = self.num_vertices_ford_fulkerson.get()
        source_node = self.source_node.get()
        sink_node = self.sink_node.get()

        # Generate a random weighted directed graph
        graph = nx.DiGraph()
        for u in range(num_vertices):
            for v in range(u + 1, num_vertices):
                if random.random() < 0.5:
                    graph.add_edge(u, v, capacity=random.randint(1, 10))
                    graph.add_edge(v, u, capacity=random.randint(1, 10))

        # Apply the Ford-Fulkerson algorithm
        try:
            flow_value, flow_dict = nx.maximum_flow(graph, _s=int(source_node), _t=int(sink_node))
        except nx.NetworkXError:
            messagebox.showerror("Erreur", "Noeud source ou puit invalide.")
            return

        # Display the graph
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(graph)
        nx.draw(
            graph,
            pos,
            with_labels=True,
            node_size=500,
            font_weight="bold",
        )
        plt.title(f"Flot maximal (Ford-Fulkerson) de {source_node} à {sink_node}: {flow_value}")

        # Embed the matplotlib figure in Tkinter
        self.current_figure_canvas = FigureCanvasTkAgg(plt.gcf(), self.root)
        self.current_figure_canvas.get_tk_widget().pack(pady=10)
        plt.close()

    def generate_and_apply_potentiel_metra(self):
        """Generate a task graph, display a table, and plot the graph."""
        # Clear previous results first
        for widget in self.pm_table_frame.winfo_children():
            widget.destroy()
        for widget in self.pm_graph_frame.winfo_children():
            widget.destroy()
        
        num_tasks = self.n.get()
    
        # Validate input
        if num_tasks <= 0:
            messagebox.showerror("Erreur", "Le nombre de tâches doit être supérieur à 0.")
            return
    
        # Generate a random task graph
        graph = nx.DiGraph()
        for i in range(num_tasks):
            graph.add_node(i, duration=random.randint(1, 10))
            if i > 0:
                graph.add_edge(i - 1, i)
    
        try:
            # Apply the Potentiel-Métra algorithm
            earliest_start = list(nx.topological_sort(graph))
            latest_start = list(reversed(earliest_start))
    
            # Create the table
            columns = ("Tâche", "Durée", "Dépendances", "Date au plus tôt", "Date au plus tard", "Marge")
            table = ttk.Treeview(self.pm_table_frame, columns=columns, show="headings")
    
            # Configure columns
            for col in columns:
                table.heading(col, text=col, anchor=tk.CENTER)
                table.column(col, width=120, anchor=tk.CENTER)
    
            # Style the table
            style = ttk.Style()
            style.configure("Treeview", font=("Arial", 11))
            style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
    
            # Add scrollbars
            y_scrollbar = ttk.Scrollbar(self.pm_table_frame, orient=tk.VERTICAL, command=table.yview)
            x_scrollbar = ttk.Scrollbar(self.pm_table_frame, orient=tk.HORIZONTAL, command=table.xview)
            table.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
    
            # Add data to table
            for node in graph.nodes():
                duration = graph.nodes[node]['duration']
                dependencies = ", ".join(map(str, graph.predecessors(node)))
                early_start = earliest_start.index(node)
                late_start = latest_start.index(node)
                float_time = late_start - early_start
                
                table.insert("", "end", values=(
                    node,
                    duration,
                    dependencies if dependencies else "-",
                    early_start,
                    late_start,
                    float_time
                ))
    
            # Pack the table with scrollbars
            x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
            y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            table.pack(fill=tk.BOTH, expand=True)
    
            # Display the graph
            plt.figure(figsize=(10, 6))
            pos = nx.spring_layout(graph)
            nx.draw(
                graph,
                pos,
                with_labels=True,
                node_size=2000,
                node_color="lightblue",
                font_size=12,
                font_weight="bold",
                edge_color="gray",
                width=2,
                arrows=True
            )
    
            # Add duration labels to nodes
            node_labels = nx.get_node_attributes(graph, 'duration')
            pos_attrs = {}
            for node, coords in pos.items():
                pos_attrs[node] = (coords[0], coords[1] - 0.08)
            nx.draw_networkx_labels(graph, pos_attrs, {node: f"Durée: {dur}" for node, dur in node_labels.items()})
    
            plt.title("Graphe des tâches (Potentiel-Métra)")
    
            # Embed the matplotlib figure
            self.current_figure_canvas = FigureCanvasTkAgg(plt.gcf(), self.pm_graph_frame)
            self.current_figure_canvas.get_tk_widget().pack(pady=10, fill=tk.BOTH, expand=True)
            plt.close()

        except nx.NetworkXUnfeasible:
            messagebox.showerror("Erreur", "Le graphe contient un cycle.")
            return

    def apply_nord_ouest(self):
        """Apply Nord-Ouest method and display results in the table."""
        self.create_transport_table("Nord-Ouest")
    
    def apply_moindre_cout(self):
        """Apply Moindre Coût method and display results in the table."""
        self.create_transport_table("Moindre Coût")
    
    def apply_stepping_stone(self):
        """Apply Stepping Stone method and display results in the table."""
        self.create_transport_table("Stepping Stone")

    def create_transport_table(self, method_name):
        """Create and populate the transport problem table."""
        # Clear previous table
        for widget in self.table_frame.winfo_children():
            widget.destroy()
    
        num_suppliers = self.num_suppliers.get()
        num_consumers = self.num_consumers.get()
    
        # Generate random data
        costs = np.random.randint(1, 100, size=(num_suppliers, num_consumers))
        supply = np.random.randint(50, 200, size=num_suppliers)
        demand = np.random.randint(50, 200, size=num_consumers)
    
        # Create table using ttk.Treeview
        columns = [""] + [f"D{i+1}" for i in range(num_consumers)] + ["Offre"]
        table = ttk.Treeview(self.table_frame, columns=columns, show="headings")
    
        # Configure columns
        for col in columns:
            table.heading(col, text=col)
            table.column(col, width=80, anchor=tk.CENTER)
    
        # Add data rows
        for i in range(num_suppliers):
            row_data = [f"S{i+1}"] + [str(costs[i][j]) for j in range(num_consumers)] + [str(supply[i])]
            table.insert("", tk.END, values=row_data)
    
        # Add demand row
        demand_row = ["Demande"] + [str(d) for d in demand] + [""]
        table.insert("", tk.END, values=demand_row)
    
        # Style the table
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 12))
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
    
        # Add method label
        tk.Label(
            self.table_frame,
            text=f"Méthode : {method_name}",
            font=("Arial", 14, "bold"),
            bg="#f7f9fc"
        ).pack(pady=(0, 10))
    
        # Pack table with scrollbars
        x_scrollbar = ttk.Scrollbar(self.table_frame, orient=tk.HORIZONTAL, command=table.xview)
        y_scrollbar = ttk.Scrollbar(self.table_frame, orient=tk.VERTICAL, command=table.yview)
        table.configure(xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)
    
        x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=True, fill=tk.BOTH)

    def show_transport_problem_frame(self):
        """Show the transport problem frame."""
        self.hide_all_frames()
        self.transport_problem_frame.pack(fill=tk.BOTH, expand=True)
        



if __name__ == "__main__":
    root = tk.Tk()
    app = ModernGraphApp(root)
    root.mainloop()