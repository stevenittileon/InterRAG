def detect_domain(resume_text):
    domains = {
        'data_science': ['machine learning', 'data analysis', 'statistics', 'python', 'pandas', 'numpy', 'deep learning'],
        'sde': ['software development', 'java', 'c++', 'python', 'algorithms', 'system design', 'backend', 'frontend'],
        # Add more domains and keywords as needed
    }
    resume_text_lower = resume_text.lower()
    for domain, keywords in domains.items():
        for kw in keywords:
            if kw in resume_text_lower:
                return domain
    return 'general' 