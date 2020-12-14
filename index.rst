########
Hi there
########

.. toctree::
  :maxdepth: 2
  :hidden:

  Home <self>
  CV <cv>

.. Hiding - Indices and tables
   :ref:`genindex`
   :ref:`modindex`
   :ref:`search`

I am currently a Research Staff Member in the `IBM Quantum <https://www.ibm.com/quantum-computing/>`_ team at the
T. J. Watson research lab in Yorktown Heights New York.  I work mainly in the area of
software development, with a focus on numerical methods and scientific
visualization techniques.  I also explore hardware benchmarking and verification, and occasionally
help on the ecosystem building side of things through the
`IBM Q Network <https://www.ibm.com/quantum-computing/ibm-q-network>`_.


.. container:: left-col

    I have been working in the area of numerical quantum optics for over a decade,
    starting with the creation of `QuTiP <http://qutip.org/>`_: Quantum Toolbox in Python in 2010 up to the present
    with the IBM `Qiskit <https://qiskit.org/>`_ framework.  I received my PhD in 2010 from the `Dartmouth College
    Department of Physics and Astronomy <https://physics.dartmouth.edu/>`_ under 
    `Miles Blencowe <https://physics.dartmouth.edu/people/miles-p-blencowe>`_.  In addition to numerical methods in
    quantum optics I have also explored quantum nanomechanical systems, optomechanical system in the quantum regime,
    analogue gravitational physics, and transport models for Hawking radiation.  Prior to joining IBM, I was 
    a Staff Physicist at Northrop Grumman, an Assistant Professor at `Korea University <http://physics.korea.ac.kr/>`_,
    and a postdoctoral researcher in the group of `Franco Nori <https://dml.riken.jp/>`_ at RIKEN just outside of Tokyo.


.. container:: right-col

    .. jupyter-execute::
        :hide-code:

        import requests
        from bs4 import BeautifulSoup
        r  = requests.get("https://scholar.google.com/citations?user=jh5qRs0AAAAJ")
        soup = BeautifulSoup(r.text)
        hist = soup.find(attrs={'class':'gsc_md_hist_b'})

        years = []
        citations = []
        for year_div in hist.find_all(attrs={'class':'gsc_g_t'}):
            years.append(year_div.text)
            
        for cite_div in hist.find_all(attrs={'class':'gsc_g_al'}):
            citations.append(int(cite_div.text))

        import plotly.graph_objects as go

        fig = go.Figure([go.Bar(x=years, y=citations, marker_color='#204195')])

        fig.update_xaxes(title='Year',
                            titlefont_size=14,
                            tickfont_size=12,
                            showline=True, linewidth=1,
                            )

        fig.update_yaxes(title='Citations',
                            titlefont_size=14,
                            tickfont_size=12,
                            showline=True, linewidth=1,
                            )

        total_citations = sum([int(c) for c in citations])
        fig.update_layout(xaxis_tickangle=-45,
                          plot_bgcolor='#d8d8d8',
                          title=dict(text='Google Scholar citations ({})'.format(total_citations), x=0.5),
                          title_font_size=14,
                          height=300,
                          margin=dict(
                                        l=5,
                                        r=5,
                                        b=20,
                                        t=80,
                                    ),
                          )
        
        go.FigureWidget(fig)