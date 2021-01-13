class debugger:

    import logging

    FORMAT = '%(message)s'
    logging.basicConfig(level=logging.DEBUG,
                        filename='app.log', filemode='w', format=FORMAT)
