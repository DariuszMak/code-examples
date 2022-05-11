/*
 * menu_stage.cpp
 *
 *  Created on: Mar 30, 2022
 *      Author: Darek
 */

#include "menu_stage.h"
#include "widgets/marker_widget.h"
#include "drawer.h"
#include "gui.h"

namespace gui
{

MenuStage::MenuStage()
:
m_settingsNavigationIndex(0),
m_settingEditMode(false)
{
    setRotation(rotationType);
}

MenuStage::~MenuStage()
{
    for (TSettingComponent settingComponent : m_SettingsComponents)
    {
        delete settingComponent.pValueObject;
    }
}

void MenuStage::setContext(MenuContext* menuContext)
{
    m_pMenuContext = menuContext;
}

void MenuStage::setRotation(int rotation)
{
    rotationType = rotation;

    if (rotation == ROTATION_NONE)
    {
        isVerticalMode = false;
    }
    else
    {
        isVerticalMode = true;
    }
}

void MenuStage::renderStageWithRotation()
{
    switch(rotationType)
	{
		case ROTATION_NONE:
            renderStage(m_pMenuContext->getMPGui()->getMPDisplayBuffer());
			break;
		case ROTATION_RIGHT:
            renderStage(displayVerticalBuffer);
            Drawer::rotateBufferRight(m_pMenuContext->getMPGui()->getMPDisplayBuffer(), displayVerticalBuffer);
			break;
		case ROTATION_LEFT:
            renderStage(displayVerticalBuffer);
            Drawer::rotateBufferLeft(m_pMenuContext->getMPGui()->getMPDisplayBuffer(), displayVerticalBuffer);
			break;
		default:
			break;
	}
}

void MenuStage::renderStage(uint8_t* pCanvas)
{
    renderWidgetComponents(pCanvas);

    renderSettingComponents(pCanvas);

    renderMarker(pCanvas);
}

const GUI* MenuContext::getMPGui() const
{
    return m_pGUI;
}

uint8_t MenuStage::getSettingsNavigationIndex() const
{
    return m_settingsNavigationIndex;
}

void MenuStage::setSettingsNavigationIndex(uint8_t settingsNavigationIndex)
{
    m_settingsNavigationIndex = settingsNavigationIndex;
}

void MenuStage::addSingleWidget(Widget* pWidget)
{
    if(m_WidgetsComponents.size() > MAX_WIDGET_NUMBER)
    {
        return;
    }

    TWidgetComponent twidgetComponent;
    twidgetComponent.pWidget = pWidget;

    m_WidgetsComponents.push_back(twidgetComponent);
}

void MenuStage::addWidgetCoordinates(uint8_t index, uint8_t column, uint8_t page, EHorizontalComponentPosition horizontalComponentPosition)
{
    TWidgetComponent* twidgetComponent = &m_WidgetsComponents[index];

    if(index >= m_WidgetsComponents.size())
    {
        return;
    }

    TElementPosition position;
    position.column = column;
    position.page = page;

    twidgetComponent->position = position;
    twidgetComponent->horizontalComponentPosition = horizontalComponentPosition;
}

void MenuStage::addSingleSetting(SettingWidget* pValueObject)
{
    if (m_SettingsComponents.size() > MAX_SETTING_NUMBER)
    {
        return;
    }
    TSettingComponent tsettingComponent;

    tsettingComponent.pValueObject = pValueObject;

    m_SettingsComponents.push_back(tsettingComponent);
}

void MenuStage::addSettingCoordinates(uint8_t index, uint8_t labelMarkerColumn, uint8_t labelMarkerPage, uint8_t valueMarkerColumn, uint8_t valueMarkerPage, uint8_t valueColumn, uint8_t valuePage)
{
    TSettingComponent* tsettingComponent = &m_SettingsComponents[index];

    if(index >= m_SettingsComponents.size())
    {
        return;
    }

    TElementPosition position;

    position.column = labelMarkerColumn;
    position.page = labelMarkerPage;
    tsettingComponent->labelMarkerPosition = position;

    position.column = valueMarkerColumn;
    position.page = valueMarkerPage;
    tsettingComponent->valueMarkerPosition = position;

    position.column = valueColumn;
    position.page = valuePage;
    tsettingComponent->valuePosition = position;
}

bool MenuStage::settingsNavigationMarkerIndexDecrease()
{
    bool isOnEdge = false;

    if (m_settingsNavigationIndex > 0)
    {
    	m_settingsNavigationIndex--;
    }
    else
    {
    	m_settingsNavigationIndex = m_SettingsComponents.size() - 1;
        isOnEdge = true;
    }

    return isOnEdge;
}

bool MenuStage::settingsNavigationMarkerIndexIncrease()
{
    bool isOnEdge = false;

    if (m_settingsNavigationIndex < m_SettingsComponents.size() - 1)
    {
    	m_settingsNavigationIndex++;
    }
    else
    {
    	m_settingsNavigationIndex = 0;
        isOnEdge = true;
    }

    return isOnEdge;
}

void MenuStage::renderWidgetComponents(uint8_t* pCanvas)
{
    for (std::vector<TWidgetComponent>::iterator i = m_WidgetsComponents.begin(); i != m_WidgetsComponents.end(); ++i)
    {
        uint8_t* temporaryBuffer = new uint8_t [Drawer::LOCAL_BUFFER_SIZE] {0};

        uint16_t byteCounter = i->pWidget->render(temporaryBuffer);

        if (i->horizontalComponentPosition != EHorizontalComponentPosition::CUSTOM)
        {
            i->position.column = determineColumnPosition(i->horizontalComponentPosition, byteCounter);
        }

        Drawer::writeWidgetBufferToGlobalBuffer(pCanvas, temporaryBuffer, i->position, isVerticalMode);

        delete[] temporaryBuffer;
    }

    m_WidgetsComponents.clear();
}

void MenuStage::renderSettingComponents(uint8_t* pCanvas)
{
    for (std::vector<TSettingComponent>::iterator i = m_SettingsComponents.begin(); i != m_SettingsComponents.end(); ++i)
    {
        uint8_t* temporaryBuffer = new uint8_t [Drawer::LOCAL_BUFFER_SIZE] {0};

        if(i->pValueObject != nullptr)
        {
            i->pValueObject->render(temporaryBuffer);

            Drawer::writeWidgetBufferToGlobalBuffer(pCanvas, temporaryBuffer, i->valuePosition, isVerticalMode);
        }

        delete[] temporaryBuffer;
    }
}

void MenuStage::renderMarker(uint8_t* pCanvas)
{
    if(!m_SettingsComponents.empty())
    {
        if (m_settingsNavigationIndex > m_SettingsComponents.size())
        {
        	m_settingsNavigationIndex = 0;
        }

        TElementPosition markerPosition;

        if(m_settingEditMode)
        {
            markerPosition.column = m_SettingsComponents[m_settingsNavigationIndex].valueMarkerPosition.column;
            markerPosition.page = m_SettingsComponents[m_settingsNavigationIndex].valueMarkerPosition.page;
        }
        else
        {
            markerPosition.column = m_SettingsComponents[m_settingsNavigationIndex].labelMarkerPosition.column;
            markerPosition.page = m_SettingsComponents[m_settingsNavigationIndex].labelMarkerPosition.page;
        }

        MarkerWidget markerWidget = MarkerWidget();

        uint8_t* temporaryBuffer = new uint8_t [Drawer::LOCAL_BUFFER_SIZE] {0};

        markerWidget.render(temporaryBuffer);

        Drawer::writeWidgetBufferToGlobalBuffer(pCanvas, temporaryBuffer, markerPosition, isVerticalMode, 5);

        delete[] temporaryBuffer;
    }
}

uint8_t MenuStage::determineColumnPosition(EHorizontalComponentPosition horizontalComponentPosition, size_t widgetXLength)
{
    size_t columnsNumber;

    if (isVerticalMode)
    {
        columnsNumber = Drawer::VERTICAL_DISPLAY_COLUMNS;
    }
    else
    {
        columnsNumber = Drawer::DISPLAY_COLUMNS;
    }

    int8_t centerPosition = (columnsNumber / 2U) - (widgetXLength / 2);

    if (centerPosition < 0)
    {
        centerPosition = 0;
    }

	switch(horizontalComponentPosition)
	{
        case EHorizontalComponentPosition::CENTER:
            return centerPosition;
            break;

        default:
			return 0;
	}
}

} // namespace gui
