#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_STRING_LENGTH 6

struct package
{
	char *id;
	int weight;
};

typedef struct package package;

struct post_office
{
	int min_weight;
	int max_weight;
	package *packages;
	int packages_count;
};

typedef struct post_office post_office;

struct town
{
	char *name;
	post_office *offices;
	int offices_count;
};

typedef struct town town;

void print_all_packages(town t) {
    printf("%s:\n", t.name);

    for (int i = 0; i < t.offices_count; i++) {
        post_office po;
        po = t.offices[i];

        printf("\t%d:\n", i);
        for (int j = 0; j < po.packages_count; j++) {
            package p;
            p = po.packages[j];

            printf("\t\t%s\n", p.id);
        }
    }
}

void send_all_acceptable_packages(town *source, int source_office_index,
                                  town *target, int target_office_index)
{
    post_office *from, *to;
    int returned_count;
    package *returned;

    returned_count = 0;
    returned = malloc(1);

    from = &(source->offices[source_office_index]);
    to = &(target->offices[target_office_index]);

    for (int i = 0; i < from->packages_count; i++) {
        package pkg;
        pkg = from->packages[i];

        if (pkg.weight >= to->min_weight && pkg.weight <= to->max_weight) {
            to->packages_count++;
            to->packages = (package *) realloc(to->packages, 
                                               sizeof(package)*to->packages_count);
            to->packages[to->packages_count-1] = pkg;
        } else {
            returned_count++;
            returned = (package *) realloc(returned,
                                           sizeof(package)*returned_count);
            returned[returned_count-1] = pkg;
        }
    }

    free(from->packages);
    from->packages = returned;
    from->packages_count = returned_count;
}

town *town_with_most_packages(town *towns, int towns_count) {
    int result, best;

    for (int i = 0; i < towns_count; i++) {
        int total_pkgs;
        town t;

        t = towns[i];
        total_pkgs = 0;

        for (int j = 0; j < t.offices_count; j++) {
            post_office po;
            po = t.offices[j];

            total_pkgs += po.packages_count;
        }

        if (total_pkgs > best) {
            best = total_pkgs;
            result = i;
        }
    }

    return &towns[result];
}

town *find_town(town *towns, int towns_count, char *name) {
    town *current;

    for (int i = 0; i < towns_count; i++) {
        current = &towns[i];

        if (!strcmp(current->name, name))
            break;
    }

    return current;
}

int main()
{
	int towns_count;
	scanf("%d", &towns_count);
	town* towns = malloc(sizeof(town)*towns_count);
	for (int i = 0; i < towns_count; i++) {
		towns[i].name = malloc(sizeof(char) * MAX_STRING_LENGTH);
		scanf("%s", towns[i].name);
		scanf("%d", &towns[i].offices_count);
		towns[i].offices = malloc(sizeof(post_office)*towns[i].offices_count);
		for (int j = 0; j < towns[i].offices_count; j++) {
			scanf("%d%d%d", &towns[i].offices[j].packages_count,
                  &towns[i].offices[j].min_weight,
                  &towns[i].offices[j].max_weight);
			towns[i].offices[j].packages =
                malloc(sizeof(package)*towns[i].offices[j].packages_count);
			for (int k = 0; k < towns[i].offices[j].packages_count; k++) {
				towns[i].offices[j].packages[k].id = malloc(sizeof(char) * MAX_STRING_LENGTH);
				scanf("%s", towns[i].offices[j].packages[k].id);
				scanf("%d", &towns[i].offices[j].packages[k].weight);
			}
		}
	}
	int queries;
	scanf("%d", &queries);
	char town_name[MAX_STRING_LENGTH];
	while (queries--) {
		int type;
		scanf("%d", &type);
		switch (type) {
		case 1:
			scanf("%s", town_name);
			town* t = find_town(towns, towns_count, town_name);
			print_all_packages(*t);
			break;
		case 2:
			scanf("%s", town_name);
			town* source = find_town(towns, towns_count, town_name);
			int source_index;
			scanf("%d", &source_index);
			scanf("%s", town_name);
			town* target = find_town(towns, towns_count, town_name);
			int target_index;
			scanf("%d", &target_index);
			send_all_acceptable_packages(source, source_index, target, target_index);
			break;
		case 3:
			printf("Town with the most number of packages is %s\n",
                   (*town_with_most_packages(towns, towns_count)).name);
			break;
		}
	}
	return 0;
}