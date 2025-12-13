    long_description_content_type="text/markdown",
    description='User-Agent and Referer Header SQLI Fuzzer',
    url='https://github.com/root-tanishq/userefuzz',
    author='Tanishq Rathore',
    license='MIT',
    packages=['userefuzz'],
    install_requires=['requests','colorama'],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'userefuzz = userefuzz.__main__:main'
        ]
    },
)
# auto-comment Sat 11/29/2025  2:47:30 (hotfix/models-7841) 
