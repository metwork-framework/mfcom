/**
 * Binaire qui appelle la fonction synutil_is_interaction_execution()
 *
 * @author Fabien MARTY <fabien.marty@meteo.fr>
 * @since avril 2012
 * @file echo_ok.c
 */

#include <glib.h>
#include "synutil.h"
#include <locale.h>
#include <stdio.h>

static GOptionEntry entries[] = {};

int main(int argc, char *argv[])
{
    /**
     * Variables globales
     */
    GError *error = NULL;
    GOptionContext *context;
    int res = 0;

    /**
     * Parsing de la ligne de commande
     */
    setlocale(LC_ALL, "");
    context = g_option_context_new("- return status code 0 if we guess this is an interactive execution");
    g_option_context_add_main_entries(context, entries, NULL);
    if (!g_option_context_parse (context, &argc, &argv, &error)) {
        g_print(g_option_context_get_help(context, TRUE, NULL));
        fprintf(stderr, "ERROR WHEN COMMAND LINE PARSING\n");
    }

    /**
     * Appel
     */
    gboolean is = synutil_is_interactive_execution();
    if (is == FALSE) {
        res = 1;
    }

    /**
     * Libération / sortie
     */
    return res;
}
