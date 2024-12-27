from enum import Enum
template_1 = r"""\documentclass[11pt,a4paper,sans]{moderncv}

\moderncvstyle{classic}
\moderncvcolor{blue}

\usepackage[scale=0.75]{geometry}
\setlength{\footskip}{136.00005pt}

\ifxetexorluatex
  \usepackage{fontspec}
  \usepackage{unicode-math}
  \defaultfontfeatures{Ligatures=TeX}
  \setmainfont{Latin Modern Roman}
  \setsansfont{Latin Modern Sans}
  \setmonofont{Latin Modern Mono}
  \setmathfont{Latin Modern Math} 
\else
  \usepackage[T1]{fontenc}
  \usepackage{lmodern}
\fi

\usepackage[english]{babel}

\name{John}{Doe}
\title{Résumé title}
\born{4 July 1776}
\address{street and number}{postcode city}{country}
\phone[mobile]{+1~(234)~567~890}
\phone[fixed]{+2~(345)~678~901}
\phone[fax]{+3~(456)~789~012}
\email{john@doe.org}
\homepage{www.johndoe.com}

\social[linkedin]{john.doe}
\social[xing]{john\_doe}
\social[twitter]{ji\_doe}
\social[github]{jdoe}
\social[gitlab]{jdoe}

\extrainfo{additional information}
\quote{Some quote}

\renewcommand*{\bibliographyitemlabel}{[\arabic{enumiv}]}

\begin{document}

\makecvtitle

\section{Education}
\cventry{year--year}{Degree}{Institution}{City}{\textit{Grade}}{Description}
\cventry{year--year}{Degree}{Institution}{City}{\textit{Grade}}{Description}

\section{Master thesis}
\cvitem{title}{\emph{Title}}
\cvitem{supervisors}{Supervisors}
\cvitem{description}{Short thesis abstract}

\section{Experience}
\cventry{year--year}{Job title}{Employer}{City}{}{General description no longer than 1--2 lines.\newline{}
Detailed achievements:
\begin{itemize}
\item Achievement 1
\item Achievement 2 (with sub-achievements)
  \begin{itemize}
  \item Sub-achievement (a);
  \item Sub-achievement (b), with sub-sub-achievements;
    \begin{itemize}
    \item Sub-sub-achievement i;
    \item Sub-sub-achievement ii;
    \item Sub-sub-achievement iii;
    \end{itemize}
  \item Sub-achievement (c);
  \end{itemize}
\item Achievement 3
\item Achievement 4
\end{itemize}}
\cventry{year--year}{Job title}{Employer}{City}{}{Description line 1\newline{}Description line 2\newline{}Description line 3}
\subsection{Miscellaneous}
\cventry{year--year}{Job title}{Employer}{City}{}{Description}

\section{Languages}
\cvitemwithcomment{Language 1}{Skill level}{Comment}
\cvitemwithcomment{Language 2}{Skill level}{Comment}
\cvitemwithcomment{Language 3}{Skill level}{Comment}
\cvitemwithcomment{Language 4}{Skill level}{Comment}

\section{Computer skills}
\cvdoubleitem{category 1}{XXX, YYY, ZZZ}{category 4}{XXX, YYY, ZZZ}
\cvdoubleitem{category 2}{XXX, YYY, ZZZ}{category 5}{XXX, YYY, ZZZ}
\cvdoubleitem{category 3}{XXX, YYY, ZZZ}{category 6}{XXX, YYY, ZZZ}

\section{Skill matrix}
\cvitem{Skill matrix}{Alternatively, provide a skill matrix to show off your skills}

\cvskilllegend*[1em]{}

\cvskillhead[-0.1em]

\cvskillentry*{Language:}{3}{Python}{2}{I'm so experienced in Python and have realised a million projects. At least.}
\cvskillentry{}{2}{Lilypond}{14}{So much sheet music! Man, I'm the best!}
\cvskillentry{}{3}{\LaTeX}{14}{Clearly I rock at \LaTeX}
\cvskillentry*{OS:}{3}{Linux}{2}{I only use Archlinux btw}
\cvskillentry*[1em]{Methods}{4}{SCRUM}{8}{SCRUM master for 5 years}

\section{Interests}
\cvitem{hobby 1}{Description}
\cvitem{hobby 2}{Description}
\cvitem{hobby 3}{Description}

\section{Extra 1}
\cvlistitem{Item 1}
\cvlistitem{Item 2}
\cvlistitem{Item 3. This item is particularly long and therefore normally spans over several lines. Did you notice the indentation when the line wraps?}

\section{Extra 2}
\cvlistdoubleitem{Item 1}{Item 4}
\cvlistdoubleitem{Item 2}{Item 5\cite{book2}}
\cvlistdoubleitem{Item 3}{Item 6. Like item 3 in the single column list before, this item is particularly long to wrap over several lines.}

\nocite{*}
\bibliographystyle{plain}
\bibliography{publications}

\end{document}"""

template_2 = r"""\documentclass[letterpaper,10pt]{article}
\usepackage[empty]{fullpage}
\usepackage{titlesec,enumitem,hyperref,fancyhdr,multicol,xcolor,lastpage}
\usepackage{CormorantGaramond,charter}

\definecolor{accentTitle}{HTML}{000000}
\definecolor{accentText}{HTML}{000000}
\definecolor{accentLine}{HTML}{000000}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\addtolength{\oddsidemargin}{-0.7in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1.19in}
\addtolength{\topmargin}{-0.7in}
\addtolength{\textheight}{1.4in}

\setlength{\multicolsep}{-3pt}
\setlength{\footskip}{3.7pt}
\raggedbottom
\raggedright

\titleformat{\section}{
  \vspace{-5pt}
  \color{accentText}\raggedright\large\bfseries
}{}{0em}{}[\color{accentLine}\titlerule]

\newcommand{\documentTitle}[2]{
  \begin{center}
    {\Huge\color{accentTitle} #1}
    \vspace{10pt}
    {\color{accentLine}\hrule}
    \vspace{2pt}
    \footnotesize{#2}
    \vspace{2pt}
    {\color{accentLine}\hrule}
  \end{center}
}

\newcommand{\heading}[2]{\hspace{10pt}#1\hfill#2\\}
\newcommand{\headingBf}[2]{\heading{\textbf{#1}}{\textbf{#2}}}
\newcommand{\headingIt}[2]{\heading{\textit{#1}}{\textit{#2}}}

\newenvironment{resume_list}{
  \vspace{-7pt}
  \begin{itemize}[itemsep=-2px, parsep=1pt, leftmargin=30pt]
}{\end{itemize}}

\renewcommand\labelitemi{--}

\begin{document}

\documentTitle{[Your Name]}{
  \href{tel:[Your Phone Number]}{[Your Phone Number]} ~ | ~
  \href{mailto:[Your Email]}{[Your Email]} ~ | ~
  \href{https://linkedin.com/in/[Your LinkedIn Handle]}{linkedin.com/in/[Your LinkedIn Handle]} ~ | ~
  \href{https://github.com/[Your GitHub Handle]}{github.com/[Your GitHub Handle]}
}

\section{Summary}
[Provide a brief summary of your professional background and key skills.]

\section{Experience}
\headingBf{[Company Name]}{[Start Date] -- [End Date]}
\headingIt{[Job Title]}{}
\begin{resume_list}
  \item [Describe a key responsibility or achievement in this role.]
  \item [List additional accomplishments or contributions.]
\end{resume_list}

\headingBf{[Company Name]}{[Start Date] -- [End Date]}
\headingIt{[Job Title]}{}
\begin{resume_list}
  \item [Highlight a significant task or result from this position.]
\end{resume_list}

\section{Skills}
\begin{multicols}{2}
\begin{itemize}[itemsep=0px, parsep=1pt, left=10pt, labelsep=10pt, align=left]
  \item[\textbf{Languages}] [List programming languages]
  \item[\textbf{Frameworks}] [List frameworks or libraries]
  \item[\textbf{Databases}] [List databases]
  \item[\textbf{DevOps}] [List DevOps tools or practices]
  \item[\textbf{Tools}] [List development tools]
\end{itemize}
\end{multicols}

\section{Education}
\headingBf{[University Name]}{}
\headingIt{[Degree and Field of Study]}{[Graduation Date]}

\section{Certifications}
\begin{resume_list}
  \item [Certification Name]
  \item [Certification Name]
\end{resume_list}

\section{Projects}
\headingBf{[Project Title]}{[Organization or Context]}
\begin{resume_list}
  \item [Briefly describe the project, its goal, and your contribution.]
\end{resume_list}

\headingBf{[Project Title]}{[Organization or Context]}
\begin{resume_list}
  \item [Summarize the project and its outcomes.]
\end{resume_list}

\end{document}
"""

harshibar_template = r"""
\documentclass[letterpaper,11pt]{article}
\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\usepackage{fontawesome5}
\usepackage[scale=0.90,lf]{FiraMono}

\definecolor{light-grey}{gray}{0.83}
\definecolor{dark-grey}{gray}{0.3}
\definecolor{text-grey}{gray}{.08}

\DeclareRobustCommand{\ebseries}{\fontseries{eb}\selectfont}
\DeclareTextFontCommand{\texteb}{\ebseries}
\usepackage{contour}
\usepackage[normalem]{ulem}
\renewcommand{\ULdepth}{1.8pt}
\contourlength{0.8pt}
\newcommand{\myuline}[1]{
  \uline{\phantom{#1}}
  \llap{\contour{white}{#1}}
}


\usepackage{tgheros}
\renewcommand*\familydefault{\sfdefault} 
\usepackage[T1]{fontenc}


\pagestyle{fancy}
\fancyhf{} 
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

\addtolength{\oddsidemargin}{-0.5in}
\addtolength{\evensidemargin}{0in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-.5in}
\addtolength{\textheight}{1.0in}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}
\titleformat {\section}{
    \bfseries \vspace{2pt} \raggedright \large 
}{}{0em}{}[\color{light-grey} {\titlerule[2pt]} \vspace{-4pt}]

\newcommand{\resumeItem}[1]{
  \item\small{
    {#1 \vspace{-1pt}}
  }
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-1pt}\item
    \begin{tabular*}{\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{#1} & {\color{dark-grey}\small #2}\vspace{1pt}\\ 
      \textit{#3} & {\color{dark-grey} \small #4}\\ 
    \end{tabular*}\vspace{-4pt}
}

\newcommand{\resumeSubSubheading}[2]{
    \item
    \begin{tabular*}{\textwidth}{l@{\extracolsep{\fill}}r}
      \textit{\small#1} & \textit{\small #2} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeProjectHeading}[2]{
    \item
    \begin{tabular*}{\textwidth}{l@{\extracolsep{\fill}}r}
      #1 & {\color{dark-grey}} \\
    \end{tabular*}\vspace{-4pt}
}

\newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}

\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}
\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{0pt}}

\color{text-grey}
\begin{document}
\begin{center}
    \textbf{\Huge Harshibar} \\ \vspace{5pt}
    \small \faPhone* \texttt{555.555.5555} \hspace{1pt} $|$
    \hspace{1pt} \faEnvelope \hspace{2pt} \texttt{hello@email.com} \hspace{1pt} $|$ 
    \hspace{1pt} \faYoutube \hspace{2pt} \texttt{harshibar} \hspace{1pt} $|$
    \hspace{1pt} \faMapMarker* \hspace{2pt}\texttt{U.S. Citizen}
    \\ \vspace{-3pt}
\end{center}
\section{EXPERIENCE}
  \resumeSubHeadingListStart

    \resumeSubheading
      {YouTube}{Aug. 2019 -- Present}
      {Creator (\href{https://www.youtube.com/c/harshibar}{\myuline {@harshibar}})}{San Francisco, CA}
      \resumeItemListStart
        \resumeItem{Grew channel to \textbf{60k subscribers in 1.5 years}; created 80+ videos on tech and productivity}
        \resumeItem{Conducted A/B testing on titles and thumbnails; \textbf{increased video impressions by 2.5M} in 3 months}
         \resumeItem{Designed a Notion workflow to streamline video production and roadmapping; boosted productivity by 20\%}
        \resumeItem{\textbf{Partnered with brands like Skillshare and Squarespace} to expand their outreach via sponsorships}
        \resumeItem{\textbf{Highlights}:
            \href{https://www.youtube.com/watch?v=HhWUjp5pD0g}{\myuline {The Problem with Productivity Apps}}, \href{https://www.youtube.com/watch?v=ms4cWMsOITs}{\myuline {Obsidian App Review}},
            \href{https://www.youtube.com/watch?v=PkDbkyIR44w}{\myuline {Not-So-Minimal Desk Setup}}}
      \resumeItemListEnd

    \resumeSubheading
      {Google Verily}{Aug. 2018 -- Sept. 2019}
      {Software Engineer}{San Francisco, CA}
      \resumeItemListStart
        \resumeItem{\textbf{Led front-end development} of a dashboard to process 50k blood samples and detect early-stage cancer}
        \resumeItem{Rebuilt a Quality Control product with input from 20 cross-functional stakeholders, \textbf{saving \$1M annually}}
        \resumeItem{Spearheaded product development of a new lab workflow tool, leading to a 40\% increase in efficiency; \\ shadowed 10 core users, iterated on design docs, and implemented the solution with one engineer}

    \resumeItemListEnd

    \resumeSubheading
      {Amazon}{May 2017 -- Aug. 2017}
      {Software Engineering Intern}{Seattle, WA}
      \resumeItemListStart
        \resumeItem{Worked on the Search Customer Experience Team; \textbf{received a return offer} for a full-time position}
        \resumeItem{\textbf{Shipped a new feature to 2M+ users} to improve the search experience for movie series-related queries}
        \resumeItem{Built a back-end database service in Java and implemented a front-end UI to support future changes}
      \resumeItemListEnd

  \resumeSubHeadingListEnd
\section{PROJECTS}
    \resumeSubHeadingListStart
      \resumeProjectHeading
          {\textbf{Hyku Consulting}} {Sept. 2019 -- Mar. 2021}
          \resumeItemListStart
            \resumeItem{Mentored 15 students towards acceptance at top US boarding schools; achieved \textbf{100\% success rate}}
            \resumeItem{Designed a \textbf{collaborative learning ecosystem} for students and parents with Trello, Miro, and Google Suite}
          \resumeItemListEnd
          
        \resumeProjectHeading
          {\textbf{Minimal Icon Pack}}{Sept. 2020 -- Nov. 2020}
          \resumeItemListStart
            \resumeItem{Designed and released 100+ minimal iOS and Android icons from scratch using Procreate and Figma}
            \resumeItem{Marketed the product and design process on {\href{https://www.youtube.com/watch?v=Ju32r7QJCzk}{\myuline {YouTube}}}; accumulated over \textbf{\$250 in sales} on {\href{https://gumroad.com/l/icons-by-harshibar}{\myuline {Gumroad}}}}
          \resumeItemListEnd
          
      \resumeProjectHeading
         {\textbf{CommonIntern}}{Sept. 2019 -- May 2020}
          \resumeItemListStart
            \resumeItem{Built a Python script to automatically apply to jobs on Glassdoor using BeautifulSoup and Selenium}
            \resumeItem{\textbf{500 stars on \href{https://github.com/harshibar/common-intern}{\myuline {GitHub}}}; featured on {\href{https://hackaday.com/2020/05/30/job-application-script-automates-the-boring-stuff-with-python}{\myuline {Hackaday}}}; made the front page of {\href {https://www.reddit.com/r/Python/comments/gpaegj/i_was_tired_of_opening_100s_of_tabs_for/?utm_source=share}{\myuline {r/python}}} and {\href {https://www.reddit.com/r/programming/comments/dcmbzx/i_was_tired_of_opening_100s_of_tabs_for/}{\myuline {r/programming}}}}
          \resumeItemListEnd
          
    \resumeSubHeadingListEnd
\section {EDUCATION}
  \resumeSubHeadingListStart
    \resumeSubheading
      {Wellesley College}{Aug. 2014 -- May 2018}
      {Bachelor of Arts in Computer Science and Pre-Med}{Wellesley, MA}
      	\resumeItemListStart
    	\resumeItem {\textbf{Coursework}: Data Structures, Algorithms, Databases, Computer Systems, Machine Learning}
        \resumeItem 
            {\textbf{Research}: MIT Graybiel Lab (published author), MIT Media Lab (analyzed urban microbe spread)}
        \resumeItemListEnd
  \resumeSubHeadingListEnd
\section{SKILLS}
 \begin{itemize}[leftmargin=0in, label={}]
    \small{\item{
     \textbf{Languages} {: Python, JavaScript (React.js), HTML/CSS, SQL (PostgreSQL, MySQL)}\vspace{2pt} \\
     \textbf{Tools}     {: Figma, Notion, Jira, Trello, Miro, Google Analytics, GitHub, DaVinci Resolve, OBS}
    }}
 \end{itemize}
\end{document}

"""


mteck_resume = r"""
%%%%
% MTecknology's Resume
%%%%
% Author: Michael Lustfield
% License: CC-BY-4
% - https://creativecommons.org/licenses/by/4.0/legalcode.txt
%%%%

\documentclass[letterpaper,10pt]{article}
%%%%%%%%%%%%%%%%%%%%%%%
%% BEGIN_FILE: mteck.sty
%% NOTE: Everything between here and END_FILE can
%% be relocated to "mteck.sty" and then included with:
%\usepackage{mteck}

% Dependencies
% NOTE: Some packages (lastpage, hyperref) require second build!
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage{fontawesome5}
\usepackage{multicol}
\usepackage{bookmark}
\usepackage{lastpage}

% Sans-Serif
%\usepackage[sfdefault]{FiraSans}
%\usepackage[sfdefault]{roboto}
%\usepackage[sfdefault]{noto-sans}
%\usepackage[default]{sourcesanspro}

% Serif
\usepackage{CormorantGaramond}
\usepackage{charter}

% Colors
% Use with \color{Name}
% Can wrap entire heading with {\color{accent} [...] }
\usepackage{xcolor}
\definecolor{accentTitle}{HTML}{0e6e55}
\definecolor{accentText}{HTML}{0e6e55}
\definecolor{accentLine}{HTML}{a16f0b}

% Misc. Options
\pagestyle{fancy}
\fancyhf{}
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\urlstyle{same}

% Adjust Margins
\addtolength{\oddsidemargin}{-0.7in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1.19in}
\addtolength{\topmargin}{-0.7in}
\addtolength{\textheight}{1.4in}

\setlength{\multicolsep}{-3.0pt}
\setlength{\columnsep}{-1pt}
\setlength{\tabcolsep}{0pt}
\setlength{\footskip}{3.7pt}
\raggedbottom
\raggedright

% ATS Readability
\input{glyphtounicode}
\pdfgentounicode=1

%-----------------%
% Custom Commands %
%-----------------%

% Centered title along with subtitle between HR
% Usage: \documentTitle{Name}{Details}
\newcommand{\documentTitle}[2]{
  \begin{center}
    {\Huge\color{accentTitle} #1}
    \vspace{10pt}
    {\color{accentLine} \hrule}
    \vspace{2pt}
    %{\footnotesize\color{accentTitle} #2}
    \footnotesize{#2}
    \vspace{2pt}
    {\color{accentLine} \hrule}
  \end{center}
}

% Create a footer with correct padding
% Usage: \documentFooter{\thepage of X}
\newcommand{\documentFooter}[1]{
  \setlength{\footskip}{10.25pt}
  \fancyfoot[C]{\footnotesize #1}
}

% Simple wrapper to set up page numbering
% Usage: \numberedPages
% WARNING: Must run pdflatex twice!
\newcommand{\numberedPages}{
  \documentFooter{\thepage/\pageref{LastPage}}
}

% Section heading with horizontal rule
% Usage: \section{Title}
\titleformat{\section}{
  \vspace{-5pt}
  \color{accentText}
  \raggedright\large\bfseries
}{}{0em}{}[\color{accentLine}\titlerule]

% Section heading with separator and content on same line
% Usage: \tinysection{Title}
\newcommand{\tinysection}[1]{
  \phantomsection
  \addcontentsline{toc}{section}{#1}
  {\large{\bfseries\color{accentText}#1} {\color{accentLine} |}}
}

% Indented line with arguments left/right aligned in document
% Usage: \heading{Left}{Right}
\newcommand{\heading}[2]{
  \hspace{10pt}#1\hfill#2\\
}

% Adds \textbf to \heading
\newcommand{\headingBf}[2]{
  \heading{\textbf{#1}}{\textbf{#2}}
}

% Adds \textit to \heading
\newcommand{\headingIt}[2]{
  \heading{\textit{#1}}{\textit{#2}}
}

% Template for itemized lists
% Usage: \begin{resume_list} [items] \end{resume_list}
\newenvironment{resume_list}{
  \vspace{-7pt}
  \begin{itemize}[itemsep=-2px, parsep=1pt, leftmargin=30pt]
}{
  \end{itemize}
  %\vspace{-2pt}
}

% Formats an item to use as an itemized title
% Usage: \itemTitle{Title}
\newcommand{\itemTitle}[1]{
  \item[] \underline{#1}\vspace{4pt}
}

% Bullets used in itemized lists
\renewcommand\labelitemi{--}

%% END_FILE: mteck.sty
%%%%%%%%%%%%%%%%%%%%%%


%===================%
% John Doe's Resume %
%===================%

%\numberedPages % NOTE: lastpage requires a second build
%\documentFooter{\thepage of 2} % Does similar without using lastpage
\begin{document}

  %---------%
  % Heading %
  %---------%

  \documentTitle{John Doe}{
    % Web Version
    %\raisebox{-0.05\height} \faPhone\ [redacted - web copy] ~
    %\raisebox{-0.15\height} \faEnvelope\ [redacted - web copy] ~
    %%
    \href{tel:1234567890}{
      \raisebox{-0.05\height} \faPhone\ 123-456-7890} ~ | ~
    \href{mailto:user@domain.tld}{
      \raisebox{-0.15\height} \faEnvelope\ USER@domain.tld} ~ | ~
    \raisebox{-0.05\height}{\faMapMarker\ Tallinn, Estonia} ~ | ~
    \href{https://linkedin.com/in/USER/}{
      \raisebox{-0.15\height} \faLinkedin\ linkedin.com/in/USER} ~ | ~
    \href{https://github.com/USER}{
      \raisebox{-0.15\height} \faGithub\ github.com/USER}
  }

  %---------%
  % Summary %
  %---------%

  \tinysection{Summary}
  Simplified version of a monstrosity that I built back in college using current best practices.

  %--------%
  % Skills %
  %--------%

  \section{Skills}
	
  \begin{multicols}{2}
	  \begin{itemize}[itemsep=-2px, parsep=1pt, leftmargin=10pt, label={}]
		  \item \textbf{Programming Languages:}  Python, JavaScript, Go, Java, C++
		  \item \textbf{Frameworks \& Libraries:} Django, React.js, Node.js, Spring Boot
		  \item \textbf{Databases:} MySQL, PostgreSQL, MongoDB
		  \item \textbf{Cloud \& DevOps:} AWS, Terraform, Docker, Kubernetes, CI/CD pipelines
		  \item \textbf{Tools:} Git, JIRA, Jenkins, Elasticsearch, Redis
		\end{itemize}
	\end{multicols}
  
  %------------%
  % Experience %
  %------------%

  \section{Experience}

  \headingBf{[Company name]}{[Date range]}
  \headingIt{[Role]}{[Location]}
  \begin{resume_list}
    \item Managed virtualized server environment spanning multiple data centers
    \item Oversaw migration of critical business applications to cloud-based platforms
    \item Configured and monitored network security measures, including firewalls and intrusion detection systems
    \item Implemented multi-factor authentication for remote access to company systems
    \item Streamlined patch management process, reducing vulnerabilities and downtime
    \item Conducted regular vulnerability assessments and penetration testing
    \item Automated server provisioning and configuration management tasks
    \item Maintained documentation for IT policies and procedures
    \item Coordinated responses to cybersecurity incidents with internal teams and external vendors
  \end{resume_list}

  %-----------%
  % Education %
  %-----------%

  \section{Education}

  \headingBf{State University}{}
  \headingIt{Bachelor of Science in Computer Information Systems}{}
  \headingIt{Minors: Networking ; Network Security}{}

  \vspace{5pt}
  \headingBf{Certifications}{}
  \begin{resume_list}
    \item Salt \hspace{2pt}- SaltStack Certified Engineer
    \item GCP - Professional Cloud Architect
  \end{resume_list}

  %----------------------------%
  % Extracurricular Activities %
  %----------------------------%

  \section{Projects}

  \headingBf{Hospital / Health Science IRB}{Mar 2015 -- Present}
  \begin{resume_list}
    \item Served as non-scientific/unaffiliated patient-representative
    \item Reviewed patient consent forms for completeness, accuracy, and clarity
    \item Became familiar with industry standards and regulations (OHRP, HIPAA)
  \end{resume_list}

  \headingBf{Debian Linux}{Jan 2001 -- Present}
  \begin{resume_list}
    \item Maintained packages in Debian repositories
    \item Reviewed and sponsored packages on behalf of prospective Developers
    \item Resolved bugs reported in bug tracking system
  \end{resume_list}

\end{document}
"""



# Define name of classes
class ResumeTemplate(str, Enum):
  Blue_Modern_CV = "Blue Modern CV"
  One_page_Simple_CV = "One_page Simple CV"
  MTeck_resume = "MTeck's Resume"

# Define details of classes
Template_Details = {
  ResumeTemplate.Blue_Modern_CV: {
    'num_pages': 2,
    'structure': template_1,
    'compiler': 'xelatex',
    'version': 'texlive2020'
  },
  ResumeTemplate.One_page_Simple_CV: {
    'num_pages': 1,
    'structure': template_2,
    'compiler': 'pdflatex',
    'version': 'texlive2020'
  },
  ResumeTemplate.MTeck_resume: {
    'num_pages': 2,
    'structure': mteck_resume,
    'compiler': 'pdflatex',
    'version': 'texlive2020'
  }
}

mohammad_sf_resume = """
Mohammad Soleymani Far
Email: msoleymanifar72@gmail.com
LinkedIn: https://www.linkedin.com/in/mohammad-sf/
Phone: +3726027348
Location: Tallinn, Estonia
**Summary**
A seasoned software engineer with over 10 years in back-end development for high-traffic applications (+30 million users),
and 7+ years of technical leadership, also experienced in DevOps and cloud engineering.
**Experiences**
Role: Senior Software Engineer (Contractor)
Company: Unity Ads
Location: Helsinki, Finland
Date: 10/2023 - 01/2024
- Tuned the algorithms related to calculate CPI (Cost per Install)
- Developed some new algorithms to calculate Dynamic CPI
- Deployed new versions to the production
- Monitored performance of production
- Tuned the dev and production monitoring panels
--------------------------------------------
Role: Senior Back-end Engineer(Contractor)
Company: Straumann Group
Location: Amsterdam, Netherlands
Date: 06/2023 - 12/2023
- Developed the APIs related to the TSC (Tooth Shape Completion) Team
- Attended in Data engineering development parts
- Developed some ETL tools for the AI/ML/Data-analysis teams
- Monitored the performance of software in a production environment
- Tuned the performance of code by profiling and removing useless resource-consuming codes
- Reviewed codes of teammates
- Deployed codes to the production environment
--------------------------------------------
Role: Tech Lead
Company: Kiosk Crypto Exchange
Location: Tehran, Iran
Date:08/2022 - 09/2023
- Supervised the code review, deployment, and QA workflows ensuring consistent code quality and timely deployments
- Provided regular 1:1 meetings with technical staff and tailored quarterly growth plans for each person based on their
weaknesses
- Defined coding standards and developed automation for checking these standards in the pipeline
- Accelerated development speed and launched the project within a month of joining
- Streamlined the recruitment process of the company by providing a good hiring plan and a good recruiting flow
- Attended to the development of the order book component
- Integrated different block-chain networks such as Tron into the back-end part of the exchange
- Tuned the JVM resource consumptions by defining limits in the JVM configurations which led to 80% reduction in RAM usage
and 50% reduction of CPU usage
--------------------------------------------
Role: Co-Founder & Software Engineer
Company: Quiz of Kings
Location: Tehran, Iran
Date: 05/2015 - 07/2022
Quiz of Kings is the most popular online Trivia game with more than 30 million unique installs, published in North America and MENA regions.
- Architected and executed a resilient code and infrastructure framework that reliably supported over 30 million users, with
500K daily active and 50K concurrent users
- Led Technical staff of cross-functional teams (Question Factory, Growth, etc)
- Led the technical recruitment team resulting in hiring engineers for different departments
- Provided a pipeline for technical recruitment of the company
- Created a robust technical workflow, including code reviews, testing pipelines, and deployment strategies.
- Developed and maintained more than 200 different APIs, and nearly 15 microservices using Java, PHP, Golang, and
TypeScript languages and utilizing the DDD approach.
- Developed an event-driven microservice named “Question Factory” enabling users to write, edit, and review each other’s
questions leading to the game becoming viral 3 times and increasing 50% in revenue.
- Achieved 80% infra cost savings by migrating and optimizing the backend from PHP, Symfony 2.6, MySQL stack to Golang,
Gin, and sharded MongoDB stack.
- Developed Back-Office parts of the project using React JS, Angular JS, and Metronic.
**Skills**
Golang, TypeScript, NodeJS, ExpressJS, Gin, AWS, GCP, Docker, Kubernetes, GraphQL, PHP, Symfony, Laravel, Ansible, Elastic
Search, Redis, MySQL, MongoDB, Helm, TDD, BDD, Test, Pipeline, CI/CD
**Education**
Computer Engineering
Amirkabir University of Technology (Tehran Polytechnic)
04/2016
Tehran, Iran
"""
john_doe_legal_authorization = """
  eu_work_authorization: Yes
  us_work_authorization: Yes
  requires_us_visa: Yes
  requires_us_sponsorship: Yes
  requires_eu_visa: No
  legally_allowed_to_work_in_eu: Yes
  legally_allowed_to_work_in_us: Yes
  requires_eu_sponsorship: No
  canada_work_authorization: Yes
  requires_canada_visa: No
  legally_allowed_to_work_in_canada: Yes
  requires_canada_sponsorship: No
  uk_work_authorization: Yes
  requires_uk_visa: No
  legally_allowed_to_work_in_uk: Yes
  requires_uk_sponsorship: No
  """

john_doe_preferences = """
remote_work: Yes
in_person_work: No
open_to_relocation: No
"""