#include <stdio.h>
#include <stdlib.h>

struct Node {
    float position;
    float speed;
    float time;
    struct Node* next;
};

/*return meeting position for two cars*/
float meeting_position_calculation(float pos1, float pos2, float spd1, float spd2)
{
    return pos1 + spd1 * ((pos1 - pos2) / (spd2 - spd1));
}

float meeting_time_calculation(float pos1, float pos2, float spd1, float spd2)
{
    return (pos1 - pos2) / (spd2 - spd1);
}


int carFleet(int target, int *position, int positionSize, int *speed, int speedSize)
{
    int position_copy[positionSize];
    int position_sorted_index[positionSize];

    for(int i = 0; i < positionSize; i++)
    {
        position_copy[i] = position[i];
    }

    for(int i = 0; i < positionSize; i++)
    {

        int max_position = position_copy[0];
        int max_position_index = 0;

        for (int j = 0; j < positionSize; j++)
        {
            if (position_copy[j] > max_position){
                max_position = position_copy[j];
                max_position_index = j;
            }
        }

        position_copy[max_position_index] = -1;
        position_sorted_index[i] = max_position_index;


    }


    struct Node* fleet = NULL;

    for (int i = 0; i < positionSize; i++)
    {
        struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
        new_node->position = (float)position[position_sorted_index[i]];
        new_node->speed = (float)speed[position_sorted_index[i]];
        new_node->time = 0;
        new_node->next = fleet;
        fleet = new_node;

        if(fleet->next != NULL) {
            if(fleet->speed > fleet->next->speed) {
                float meeting_position = meeting_position_calculation(fleet->next->position, fleet->position, fleet->next->speed, fleet->speed);
                if(meeting_position <= target) {

                    struct Node* current = fleet;
                    fleet = fleet->next;
                    free(current);

                    fleet->position = meeting_position;
                }
            }
        }
    }

    int ans = 0;

    for(struct Node* ptr = fleet; ptr != NULL;ptr = ptr->next) {
        ans += 1;
    }

    return ans;

}

int main()
{
    int target = 12;
    int position[5] = {10, 8, 0, 5, 3};
    int speed[5] = {2, 4, 1, 1, 3};
    printf("%d\n", carFleet(target, position, 5, speed, 5));

    return 0;
}