from setuptools import setup

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name='beibo',
    version='0.1.3',
    description='🤖 Predict the stock market with AI 用AI预测股票市场',
    py_modules=['beibo'],
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ssantoshp/Beibo',
    author="Santosh Passoubady",
    author_email="santoshpassoubady@gmail.com",
    license='MIT',
    install_requires=[
        'darts',
        'yfinance'
    ],
)
